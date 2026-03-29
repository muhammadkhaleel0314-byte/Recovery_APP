import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from fpdf import FPDF

st.set_page_config(page_title="Recovery Portal", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: white;'>📊 Welcome to Recovery Portal</h1>
    <h3 style='text-align: center; color: Blue;'>Recovery and Overdue Portal</h3>
    <hr style='border-top: 3px solid #bbb;'>
""", unsafe_allow_html=True)

# Upload Recovery File
uploaded_file = st.file_uploader("📁 Upload Recovery File (Excel)", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df['recovery_date'] = pd.to_datetime(df['recovery_date'], errors='coerce')
    df.dropna(subset=['recovery_date'], inplace=True)
    df['day'] = df['recovery_date'].dt.day

    def get_range(day):
        if 1 <= day <= 10:
            return "1-10"
        elif 11 <= day <= 20:
            return "11-20"
        elif 21 <= day <= 31:
            return "21-31"
        return "Unknown"

    df['range'] = df['day'].apply(get_range)

    st.write("### 📄 Complete Recovery Data")
    st.dataframe(df)

    # Summary
    summary = df.groupby(['branch_id', 'range']).agg({
        'amount': 'sum',
        'receipt_no': 'count'
    }).reset_index()

    branch_totals = df.groupby('branch_id')['amount'].sum().reset_index().rename(columns={'amount': 'total_amount'})
    summary = summary.merge(branch_totals, on='branch_id')
    summary['percentage'] = (summary['amount'] / summary['total_amount']) * 100

    st.subheader("📊 Branch-wise Recovery Summary")
    st.dataframe(summary.style.format({
        'amount': 'Rs {:,.0f}',
        'percentage': '{:.2f}%'
    }))

    # Chart
    st.subheader("📈 Recovery Chart by Date Range")
    fig = px.bar(summary, x='branch_id', y='amount', color='range',
                 barmode='group',
                 text=summary['percentage'].apply(lambda x: f"{x:.1f}%"),
                 labels={'amount': 'Amount Recovered', 'branch_id': 'Branch'})
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title="Branch", yaxis_title="Amount", legend_title="Date Range")
    st.plotly_chart(fig, use_container_width=True)

    # Pivot Table
    st.subheader("📌 Pivot Table (Branch → Project → Date)")
    pivot_df = df.groupby(['branch_id', 'project', 'recovery_date']).agg(
        Receipts=('receipt_no', 'count'),
        Amount=('amount', 'sum')
    ).reset_index()

    st.dataframe(pivot_df)

    # PDF Class
    class PDF(FPDF):
        def header(self):
            pass
        def footer(self):
            pass

    # Branch-wise PDF downloads
    st.subheader("📥 Download Branch-wise Pivot Table PDFs")
    for branch, branch_df in pivot_df.groupby('branch_id'):
        branch_pdf = PDF()
        branch_pdf.set_auto_page_break(auto=True, margin=15)
        branch_pdf.add_page()
        branch_pdf.set_font("Arial", 'B', 14)
        branch_pdf.cell(0, 10, f"Branch: {branch}", ln=True, align='C')

        branch_total_amount = 0
        branch_total_receipts = 0

        for project, proj_df in branch_df.groupby('project'):
            branch_pdf.set_font("Arial", 'B', 12)
            branch_pdf.cell(0, 8, f"Project: {project}", ln=True)

            # Table Header
            branch_pdf.set_font("Arial", 'B', 10)
            branch_pdf.cell(40, 8, "Date", border=1, align='C')
            branch_pdf.cell(40, 8, "Receipts", border=1, align='C')
            branch_pdf.cell(40, 8, "Amount", border=1, align='C')
            branch_pdf.ln()

            project_total_amount = 0
            project_total_receipts = 0

            branch_pdf.set_font("Arial", '', 10)
            for _, row in proj_df.iterrows():
                date_str = row['recovery_date'].strftime('%Y-%m-%d') if pd.notnull(row['recovery_date']) else ''
                branch_pdf.cell(40, 8, date_str, border=1)
                branch_pdf.cell(40, 8, str(row['Receipts']), border=1, align='C')
                branch_pdf.cell(40, 8, f"Rs {row['Amount']:,.0f}", border=1, align='R')
                branch_pdf.ln()
                project_total_receipts += row['Receipts']
                project_total_amount += row['Amount']

            # Project total
            branch_pdf.set_font("Arial", 'B', 10)
            branch_pdf.cell(40, 8, "Project Total", border=1)
            branch_pdf.cell(40, 8, str(project_total_receipts), border=1, align='C')
            branch_pdf.cell(40, 8, f"Rs {project_total_amount:,.0f}", border=1, align='R')
            branch_pdf.ln(10)

            branch_total_receipts += project_total_receipts
            branch_total_amount += project_total_amount

        # Branch total
        branch_pdf.set_font("Arial", 'B', 11)
        branch_pdf.cell(40, 8, "Branch Total", border=1)
        branch_pdf.cell(40, 8, str(branch_total_receipts), border=1, align='C')
        branch_pdf.cell(40, 8, f"Rs {branch_total_amount:,.0f}", border=1, align='R')

        pdf_bytes = branch_pdf.output(dest='S').encode('latin1')
        st.download_button(
            label=f"📥 Download PDF for Branch {branch}",
            data=pdf_bytes,
            file_name=f"Branch_{branch}.pdf",
            mime="application/pdf"
        )
st.subheader("📥 Upload Due List and Recovery File for Overdue Detection")

dolist_file = st.file_uploader("📄 Due List Upload", type=["xlsx"], key="dolist")
recovery_file2 = st.file_uploader("📄 Recovery File Upload", type=["xlsx"], key="recovery2")

if dolist_file and recovery_file2:
    dolist_df = pd.read_excel(dolist_file)
    recovery_df2 = pd.read_excel(recovery_file2)

    dolist_df['Sanction No'] = dolist_df['Sanction No'].astype(str).str.strip()
    recovery_df2['Sanction No'] = recovery_df2['Sanction No'].astype(str).str.strip()

    overdue_df = dolist_df[~dolist_df['Sanction No'].isin(recovery_df2['Sanction No'])]
    st.subheader("❗ Overdue List")
    st.write(f"🔢 Total Overdue: {len(overdue_df)}")
    st.dataframe(overdue_df)

# Final Overdue via Terabyte
st.subheader("📥 Upload Terabyte File (Final Overdue)")

terabyte_file = st.file_uploader("📄 Terabyte File Upload", type=["xlsx"], key="terabyte")

if terabyte_file and 'overdue_df' in locals() and not overdue_df.empty:
    terabyte_df = pd.read_excel(terabyte_file)
    terabyte_df['Sanction No'] = terabyte_df['Sanction No'].astype(str).str.strip()
    overdue_df['Sanction No'] = overdue_df['Sanction No'].astype(str).str.strip()

    final_overdue_df = overdue_df[~overdue_df['Sanction No'].isin(terabyte_df['Sanction No'])]

    st.subheader("🚨 Final Overdue Cases")
    st.write(f"🔢 Total Final Overdue: {len(final_overdue_df)}")
    st.dataframe(final_overdue_df)

    # Full PDF: Branch-wise + Date-wise
    full_pdf = FPDF()
    full_pdf.set_auto_page_break(auto=True, margin=15)

    if 'branch_id' not in final_overdue_df.columns:
        final_overdue_df['branch_id'] = 'Unknown'

    for branch in final_overdue_df['branch_id'].unique():
        data = final_overdue_df[final_overdue_df['branch_id'] == branch]
        full_pdf.add_page()
        full_pdf.set_font("Arial", 'B', 12)
        full_pdf.cell(200, 10, txt=f"Branch: {branch}", ln=True, align='C')

        full_pdf.set_font("Arial", size=10)
        full_pdf.cell(10, 10, "Sr#", 1)
        full_pdf.cell(70, 10, "Name", 1)
        full_pdf.cell(60, 10, "Sanction No", 1)
        full_pdf.ln()

        for i, (_, row) in enumerate(data.iterrows(), start=1):
            full_pdf.cell(10, 10, str(i), 1)
            full_pdf.cell(70, 10, str(row.get('Name', '')), 1)
            full_pdf.cell(60, 10, str(row.get('Sanction No', '')), 1)
            full_pdf.ln()

    full_pdf_output = full_pdf.output(dest='S').encode('latin1')
    st.download_button("📥 Download Final Overdue PDF (Branch-wise)", full_pdf_output, "final_overdue.pdf", "application/pdf")
# 🔽 Separate Branch-wise PDF Downloads
    st.subheader("📂 Download Final Overdue Branch-wise PDFs")

    branch_pdfs = {}

    for branch in final_overdue_df['branch_id'].unique():
        branch_data = final_overdue_df[final_overdue_df['branch_id'] == branch]

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt=f"Branch: {branch}", ln=True, align='C')

        pdf.set_font("Arial", size=10)
        pdf.cell(10, 10, "Sr#", 1)
        pdf.cell(70, 10, "Name", 1)
        pdf.cell(60, 10, "Sanction No", 1)
        pdf.ln()

        for i, (_, row) in enumerate(branch_data.iterrows(), start=1):
            pdf.cell(10, 10, str(i), 1)
            pdf.cell(70, 10, str(row.get('Name', '')), 1)
            pdf.cell(60, 10, str(row.get('Sanction No', '')), 1)
            pdf.ln()

        pdf_bytes = pdf.output(dest='S').encode('latin1')
        branch_pdfs[branch] = pdf_bytes

    for branch, pdf_data in branch_pdfs.items():
        st.download_button(
            label=f"📥 Download PDF for Branch: {branch}",
            data=pdf_data,
            file_name=f"final_overdue_branch_{branch}.pdf",
            mime="application/pdf"
        )
import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------- PAGE ----------------

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.big-title {
    font-size: 35px;
    font-weight: bold;
    color: #2E86C1;
    text-align: center;
}
.card {
    padding: 15px;
    border-radius: 10px;
    background-color: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">💰 Daily Expense Tracker</div>', unsafe_allow_html=True)

# ---------------- IMAGE SLIDER ----------------
images = [
    "https://images.unsplash.com/photo-1604908554168-5c7d4c1c68f0",  # sabzi
    "https://images.unsplash.com/photo-1573246123716-6b1782bfc499",  # fruits
    "https://images.unsplash.com/photo-1586201375761-83865001e31c",  # grocery
]

# slider simulation
index = st.session_state.get("img_index", 0)

st.image(images[index], use_container_width=True)

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅️"):
        index = (index - 1) % len(images)

with col3:
    if st.button("➡️"):
        index = (index + 1) % len(images)

st.session_state["img_index"] = index

# ---------------- DATA ----------------
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Date","Item","Amount"])

df = st.session_state["data"]

# ---------------- ADD EXPENSE ----------------
st.subheader("➕ Add Expense")

with st.form("form"):
    date = datetime.now().strftime("%Y-%m-%d")
    item = st.text_input("Kya liya?")
    amount = st.number_input("Kitni amount?", min_value=0.0)

    submit = st.form_submit_button("Add")

if submit:
    new_row = pd.DataFrame([{
        "Date": date,
        "Item": item,
        "Amount": amount
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    st.session_state["data"] = df
    st.success("✅ Added")

# ---------------- SHOW ----------------
st.subheader("📊 Expense List")
st.dataframe(df, use_container_width=True)

# ---------------- TOTAL ----------------
total = pd.to_numeric(df["Amount"], errors="coerce").sum()
st.success(f"💰 Total: {total}")
     
