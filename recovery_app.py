import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

st.set_page_config(page_title="Recovery Portal", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: White;'>📊 Welcome to Recovery Portal</h1>
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
import os
import io
import zipfile
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fpdf import FPDF
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
import plotly.express as px

st.set_page_config(page_title="Recovery App", layout="wide")
st.title("🏦 Recovery & Reports App")

# --------------------
# File upload widgets (unique keys)
# --------------------
do_file = st.file_uploader("Upload Do List", type=["xlsx", "xls"], key="uploader_do")
recovery_file = st.file_uploader("Upload Recovery File", type=["xlsx", "xls"], key="uploader_recovery")
terabyte_file = st.file_uploader("Upload Terabyte File (Optional)", type=["xlsx", "xls"], key="uploader_terabyte")

# --------------------
# When Do + Recovery uploaded -> main logic
# --------------------
if do_file and recovery_file:
    # Read files
    do_df = pd.read_excel(do_file)
    recovery_df = pd.read_excel(recovery_file)

    # Normalize column names
    for df in [do_df, recovery_df]:
        df.columns = df.columns.str.strip()

    # --------------------
    # Overdue logic (Final Overdue List)
    # --------------------
    if 'Sanction No' not in do_df.columns or 'Sanction No' not in recovery_df.columns:
        st.error("Both Do List and Recovery File must contain 'Sanction No' column.")
    else:
        overdue_df = do_df[~do_df['Sanction No'].astype(str).str.strip().isin(
            recovery_df['Sanction No'].astype(str).str.strip()
        )].copy()

        st.subheader("🕒 Final Overdue List")
        st.dataframe(overdue_df)

        # Branch-wise Overdue PDF (as ZIP)
        if not overdue_df.empty:
            st.subheader("📁 Download Branch-wise Final Overdue (ZIP)")
            overdue_df.columns = overdue_df.columns.str.strip()
            branches = overdue_df['branch_id'].astype(str).unique()

            zip_buf_overdue = io.BytesIO()
            with zipfile.ZipFile(zip_buf_overdue, "a", zipfile.ZIP_DEFLATED) as zf:
                for branch in branches:
                    branch_data = overdue_df[overdue_df['branch_id'].astype(str) == str(branch)]

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=10)
                    pdf.cell(0, 10, f"Branch: {branch}", ln=True)

                    # Header
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(10, 10, "Sr#", 1)
                    pdf.cell(60, 10, "Name", 1)
                    pdf.cell(50, 10, "Sanction No", 1)
                    # include mobile if present
                    if "Mobile No" in branch_data.columns:
                        pdf.cell(50, 10, "Mobile No", 1)
                    pdf.ln()

                    pdf.set_font("Arial", size=9)
                    for i, (_, row) in enumerate(branch_data.iterrows(), start=1):
                        pdf.cell(10, 10, str(i), 1)
                        pdf.cell(60, 10, str(row.get("Name", ""))[:25], 1)
                        pdf.cell(50, 10, str(row.get("Sanction No", "")), 1)
                        if "Mobile No" in branch_data.columns:
                            pdf.cell(50, 10, str(row.get("Mobile No", "")), 1)
                        pdf.ln()

                    pdf_bytes = pdf.output(dest="S").encode("latin1")
                    zf.writestr(f"{branch}_Final_Overdue.pdf", pdf_bytes)

            zip_buf_overdue.seek(0)
            st.download_button(
                label="⬇️ Download Branch-wise Overdue ZIP",
                data=zip_buf_overdue.getvalue(),
                file_name="Final_Overdue_BranchWise.zip",
                mime="application/zip",
                key="download_overdue_zip"
            )
        else:
            st.info("No overdue records found.")

    # --------------------
    # Recovery this month / matched recoveries and summary / charts (original)
    # --------------------
    # Sanction No normalization
    do_df['Sanction No'] = do_df['Sanction No'].astype(str).str.strip()
    recovery_df['Sanction No'] = recovery_df['Sanction No'].astype(str).str.strip()

    # Parse recovery date if present
    if 'recovery_date' in recovery_df.columns:
        recovery_df['recovery_date'] = pd.to_datetime(recovery_df['recovery_date'], errors='coerce')
    else:
        # if no recovery_date column, try common names or create empty
        recovery_df['recovery_date'] = pd.NaT

    current_month = pd.Timestamp.now().month
    current_year = pd.Timestamp.now().year

    recovery_this_month = recovery_df[
        (recovery_df['recovery_date'].dt.month == current_month) &
        (recovery_df['recovery_date'].dt.year == current_year)
    ] if not recovery_df['recovery_date'].isna().all() else recovery_df.iloc[0:0]

    recovered = recovery_this_month[recovery_this_month['Sanction No'].isin(do_df['Sanction No'])]

    # Due summary per branch
    if 'branch_id' not in do_df.columns:
        do_df['branch_id'] = do_df.get('Branch', '')
    if 'branch_id' not in recovery_df.columns:
        recovery_df['branch_id'] = recovery_df.get('Branch Code', '')

    due_summary = do_df.groupby('branch_id')['Sanction No'].count().reset_index()
    due_summary.columns = ['branch_id', 'total_due']

    recovered_summary = recovered.groupby('branch_id')['Sanction No'].count().reset_index()
    recovered_summary.columns = ['branch_id', 'recovered']

    summary = due_summary.merge(recovered_summary, on='branch_id', how='left').fillna(0)
    summary['remaining'] = summary['total_due'] - summary['recovered']
    summary['recovery_percent'] = (summary['recovered'] / summary['total_due'].replace(0, pd.NA)) * 100
    summary['recovery_percent'] = summary['recovery_percent'].fillna(0)

    st.subheader("📋 Branch-wise Recovery Summary (This Month)")
    st.dataframe(summary.style.format({
        'total_due': '{:,.0f}',
        'recovered': '{:,.0f}',
        'remaining': '{:,.0f}',
        'recovery_percent': '{:.2f} %'
    }))

    # Chart: recovery percent by branch
    try:
        fig = px.bar(
            summary,
            x='branch_id',
            y='recovery_percent',
            text=summary['recovery_percent'].apply(lambda x: f"{x:.1f}%"),
            labels={'branch_id': 'Branch', 'recovery_percent': 'Recovery %'},
            title='📈 Recovery % by Branch (This Month)'
        )
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    except Exception:
        pass

    # Debugging info
    st.subheader("🛠 Debugging Info")
    st.write("Total Due List Entries:", len(do_df))
    st.write("Recovery Entries This Month:", len(recovery_this_month))
    st.write("Matched Recoveries:", len(recovered))

# --------------------
# TERABYTE SECTION (kept as originally present in your code)
# --------------------
# This block expects a terabyte upload (can be optional)
terabyte_pdf_file = st.file_uploader("Upload Terabyte Excel (for branch receipts PDF)", type=["xls", "xlsx"], key="uploader_terabyte_pdf")

if terabyte_pdf_file is not None:
    df_tera = pd.read_excel(terabyte_pdf_file)

    required_cols = ["Sanction No", "Recovery Date", "Receipt No", "Credit Amount", "Branch Code"]
    missing = [c for c in required_cols if c not in df_tera.columns]
    if missing:
        st.error(f"Uploaded Terabyte file must contain columns: {', '.join(missing)}")
    else:
        df_tera["Recovery Date"] = pd.to_datetime(df_tera["Recovery Date"], errors='coerce').dt.date
        df_tera.insert(0, "Serial No", range(1, len(df_tera) + 1))
        df_tera = df_tera[["Serial No", "Sanction No", "Recovery Date", "Receipt No", "Credit Amount", "Branch Code"]]

        st.write("### Terabyte Branch-wise Preview")
        st.dataframe(df_tera.head())

        # Branch-wise downloadable PDFs using reportlab (kept original approach)
        branches = df_tera["Branch Code"].unique()
        for branch in branches:
            branch_df = df_tera[df_tera["Branch Code"] == branch]

            st.write(f"#### Branch {branch} Summary")
            st.dataframe(branch_df)

            # Create in-memory PDF and show download button per branch
            buf = io.BytesIO()
            doc = SimpleDocTemplate(buf, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()

            elements.append(Paragraph(f"Branch Code: {branch}", styles['Heading1']))
            elements.append(Spacer(1, 12))

            table_data = [list(branch_df.columns)] + branch_df.values.tolist()
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(table)
            elements.append(Spacer(1, 20))

            # Branch summary
            branch_summary = pd.DataFrame({
                "Branch Code": [branch],
                "Total Receipts": [len(branch_df)],
                "Total Amount": [branch_df["Credit Amount"].sum()]
            })
            elements.append(Paragraph("Branch Summary", styles['Heading2']))
            branch_table = Table([list(branch_summary.columns)] + branch_summary.values.tolist())
            branch_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(branch_table)
            elements.append(Spacer(1, 20))

            # Date-wise summary
            date_summary = branch_df.groupby("Recovery Date").agg(
                Receipts_Count=("Receipt No", "count"),
                Amount_Sum=("Credit Amount", "sum")
            ).reset_index()
            elements.append(Paragraph("Date-wise Summary", styles['Heading2']))
            date_table = Table([list(date_summary.columns)] + date_summary.values.tolist())
            date_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgreen),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(date_table)

            doc.build(elements)
            buf.seek(0)

            st.download_button(
                label=f"Download Branch {branch} PDF",
                data=buf.getvalue(),
                file_name=f"branch_{branch}.pdf",
                mime="application/pdf",
                key=f"download_terabyte_{branch}"
            )

# --------------------
# NEW: Branch-wise Recovery PDFs from uploaded Recovery File
# (This is the single addition you asked for — everything else left intact)
# --------------------
# This button will be available if user uploaded a recovery_file earlier.
if 'recovery_file' in locals() or recovery_file is not None:
    # Use the uploaded recovery_file object if present
    # (We attempt to read it again safely here)
    try:
        if recovery_file is not None:
            rec_df_for_pdf = pd.read_excel(recovery_file)
        else:
            rec_df_for_pdf = None
    except Exception:
        rec_df_for_pdf = None

    if rec_df_for_pdf is not None and not rec_df_for_pdf.empty:
        st.subheader("📄 Generate Branch-wise PDFs from Recovery File")
        st.write("This will create a PDF per branch (recovery_date,amount, Name, Sanction No)")

        if st.button("⬇️ Generate Branch-wise Recovery PDFs", key="gen_recovery_pdfs_btn"):
            # Normalize and ensure columns
            rec_df = rec_df_for_pdf.copy()
            rec_df.columns = rec_df.columns.str.strip()

            # Ensure these columns exist or create empty
            for col in ["branch_id", "recovery_date", "amount", "Name", "Sanction No"]:
                if col not in rec_df.columns:
                    rec_df[col] = ""

            # Format Date column
            try:
                rec_df["Date"] = pd.to_datetime(rec_df["recovery_date"], errors='coerce').dt.strftime("%d-%m-%y")
            except Exception:
                rec_df["recovery_date"] = rec_df["recovery_date"].astype(str)

            branches = rec_df["branch_id"].astype(str).unique()
            zip_buffer = io.BytesIO()

            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zf:
                for branch in branches:
                    branch_data = rec_df[rec_df["branch_id"].astype(str) == str(branch)]

                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", "B", 14)
                    pdf.cell(0, 10, f"Branch: {branch}", ln=True, align="L")
                    pdf.ln(6)

                    # Header
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(12, 8, "Sr#", 1, 0, "C")
                    pdf.cell(50, 8, "Date", 1, 0, "C")
                    pdf.cell(40, 8, "Amount", 1, 0, "C")
                    pdf.cell(60, 8, "Name", 1, 0, "C")
                    pdf.cell(40, 8, "Sanction No", 1, 1, "C")

                    pdf.set_font("Arial", "", 9)
                    total_amount = 0.0
                    for i, (_, row) in enumerate(branch_data.iterrows(), start=1):
                        pdf.cell(12, 8, str(i), 1, 0, "C")
                        pdf.cell(50, 8, str(row.get("Date", ""))[:10], 1, 0, "C")
                        pdf.cell(40, 8, str(row.get("Amount", "")), 1, 0, "R")
                        pdf.cell(60, 8, str(row.get("Name", ""))[:25], 1, 0, "L")
                        pdf.cell(40, 8, str(row.get("Sanction No", "")), 1, 1, "C")
                        try:
                            total_amount += float(row.get("Amount", 0) if row.get("Amount", 0) != "" else 0)
                        except Exception:
                            pass

                    # Total row
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(62, 8, "Total", 1)
                    pdf.cell(40, 8, f"{total_amount:,.2f}", 1)
                    pdf.ln(8)

                    pdf_bytes = pdf.output(dest="S").encode("latin1")
                    zf.writestr(f"{branch}_Recovery.pdf", pdf_bytes)

            zip_buffer.seek(0)
            st.download_button(
                label="📦 Download Branch-wise Recovery PDFs (ZIP)",
                data=zip_buffer.getvalue(),
                file_name="Branch_Wise_Recovery_PDFs.zip",
                mime="application/zip",
                key="download_recovery_zip"
            )
    else:
        # No recovery file data to generate from
        pass

import streamlit as st
import pandas as pd
import re

st.header("📂 Merge CSV Files (Skip first 2 rows)")

def clean_colname(name):
    return re.sub(r'[^a-z0-9]', '', str(name).lower())

# --- Users select multiple CSV files ---
uploaded_files = st.file_uploader(
    "Upload your CSV files",
    type="csv",
    accept_multiple_files=True
)

merged_data = []
missing_sanction_files = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Skip first 2 rows
            df = pd.read_csv(uploaded_file, skiprows=2)

            # Clean columns
            df.columns = [clean_colname(col) for col in df.columns]

            # Check for Sanction No column
            possible_names = ["sanctionno", "sanctionnumber", "sactionno"]
            sanction_col = next((col for col in df.columns if col in possible_names), None)

            if sanction_col:
                merged_data.append(df)
            else:
                missing_sanction_files.append(uploaded_file.name)

        except Exception as e:
            st.error(f"Error reading {uploaded_file.name}: {e}")

    # --- Show warning for files without Sanction No ---
    if missing_sanction_files:
        st.warning("No 'Sanction No' column found in these files:")
        for f in missing_sanction_files:
            st.write(f"- {f}")

    # --- Merge and allow download ---
    if merged_data:
        final_df = pd.concat(merged_data, ignore_index=True)
        st.success(f"Merged {len(merged_data)} CSV files! Total rows: {len(final_df)}")

        csv_download = final_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇ Download Merged CSV",
            data=csv_download,
            file_name="merged_due_list.csv",
            mime="text/csv"
        )
else:
    st.info("Please upload at least one CSV file to merge.")

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

st.header("📑 Cheque-wise Analysis 1st And 2nd Tranch's")

uploaded_cheque = st.file_uploader("Upload Cheque-wise List", type=["xlsx", "csv"])

if uploaded_cheque:
    # Read uploaded file
    if uploaded_cheque.name.endswith(".csv"):
        cheque_df = pd.read_csv(uploaded_cheque)
    else:
        cheque_df = pd.read_excel(uploaded_cheque)

    # Required columns
    required_cols = ["branch_id", "date_disbursed", "sanction_no", "tranch_no", "member_name", "member_cnic"]
    cheque_df = cheque_df[[col for col in required_cols if col in cheque_df.columns]]

    # Name column
    cheque_df["Name"] = cheque_df["member_name"]
    cheque_df.drop(columns=["member_name"], inplace=True)

    # Convert date
    cheque_df["date_disbursed"] = pd.to_datetime(cheque_df["date_disbursed"], errors="coerce")
    today = datetime.today()
    cheque_df["Months Passed"] = cheque_df["date_disbursed"].apply(
        lambda x: relativedelta(today, x).months + relativedelta(today, x).years * 12 if pd.notnull(x) else None
    )
    cheque_df["Days Passed"] = cheque_df["date_disbursed"].apply(
        lambda x: (today - x).days if pd.notnull(x) else None
    )

    # Add House Complete, Shifted if missing
    for col in ["House Complete", "Shifted"]:
        if col not in cheque_df.columns:
            cheque_df[col] = "No"

    # Load previously saved flags if exist
    if os.path.exists("cheque_flags.csv"):
        saved_flags = pd.read_csv("cheque_flags.csv")
        cheque_df = cheque_df.merge(
            saved_flags,
            on=["sanction_no", "tranch_no"],
            how="left",
            suffixes=("", "_saved")
        )
        for col in ["House Complete", "Shifted"]:
            if f"{col}_saved" in cheque_df.columns:
                cheque_df[col] = cheque_df[f"{col}_saved"].combine_first(cheque_df[col])
                cheque_df.drop(columns=[f"{col}_saved"], inplace=True)

    # Order: branch_id ke baad Name
    cols = cheque_df.columns.tolist()
    if "branch_id" in cols and "Name" in cols:
        cols.insert(cols.index("branch_id") + 1, cols.pop(cols.index("Name")))
        cheque_df = cheque_df[cols]

    # -----------------------------
    # Editable Table
    # -----------------------------
    edited_df = st.data_editor(
        cheque_df,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "House Complete": st.column_config.SelectboxColumn(options=["Yes", "No"]),
            "Shifted": st.column_config.SelectboxColumn(options=["Yes", "No"])
        }
    )

    # -----------------------------
    # Fully Working Risk Level calculation (after edits)
    # -----------------------------
    def calc_risk(row):
        house = str(row.get("House Complete", "")).strip().lower()
        shifted = str(row.get("Shifted", "")).strip().lower()
        if house == "yes" or shifted == "yes":
            return "No Risk"
        
        months = row.get("Months Passed", 0)
        if pd.isna(months):
            return "Low"
        if months >= 4:
            return "High"
        if 2 <= months < 4:
            return "Medium"
        if 0 < months < 2:
            return "Low"
        return "Low"

    edited_df["Risk Level"] = edited_df.apply(calc_risk, axis=1)

    # -----------------------------
    # Save Flags Button
    # -----------------------------
    if st.button("💾 Save Flags"):
        edited_df[["sanction_no", "tranch_no", "House Complete", "Shifted"]].to_csv("cheque_flags.csv", index=False)
        st.success("✅ Flags saved successfully!")

    # -----------------------------
    # Branch-wise PDF with Risk Level colors
    # -----------------------------
    if st.button("⬇️ Download Branch-wise PDF Reports"):
        branches = edited_df["branch_id"].unique()
        os.makedirs("branch_pdfs", exist_ok=True)

        risk_colors = {
            "High": colors.red,
            "Medium": colors.yellow,
            "Low": colors.green,
            "No Risk": colors.lightgrey
        }

        for branch in branches:
            branch_df = edited_df[edited_df["branch_id"] == branch]
            pdf_path = f"branch_pdfs/branch_{branch}.pdf"

            tranch1 = (branch_df["tranch_no"] == 1).sum()
            tranch2 = (branch_df["tranch_no"] == 2).sum()
            pending = tranch1 - tranch2 if tranch1 > tranch2 else 0

            house_complete = branch_df["House Complete"].astype(str).str.lower().eq("yes").sum()
            shifted = branch_df["Shifted"].astype(str).str.lower().eq("yes").sum()

            risk_high = branch_df["Risk Level"].eq("High").sum()
            risk_med = branch_df["Risk Level"].eq("Medium").sum()
            risk_low = branch_df["Risk Level"].eq("Low").sum()
            risk_none = branch_df["Risk Level"].eq("No Risk").sum()

            doc = SimpleDocTemplate(pdf_path, pagesize=landscape(A4))
            styles = getSampleStyleSheet()
            elements = []

            elements.append(Paragraph(f"Branch ID: {branch}", styles["Heading1"]))
            elements.append(Spacer(1, 12))

            summary_text = f"""
            <b>Summary:</b><br/>
            1st Tranch Cases: {tranch1}<br/>
            2nd Tranch Cases: {tranch2}<br/>
            Pending (1st - 2nd): {pending}<br/>
            House Complete: {house_complete}<br/>
            Shifted: {shifted}<br/><br/>
            <b>Risk Level Summary:</b><br/>
            High Risk: {risk_high}<br/>
            Medium Risk: {risk_med}<br/>
            Low Risk: {risk_low}<br/>
            No Risk: {risk_none}<br/>
            """
            elements.append(Paragraph(summary_text, styles["Normal"]))
            elements.append(Spacer(1, 20))

            # Table with color-coded Risk Level
            data = [branch_df.columns.tolist()] + branch_df.astype(str).values.tolist()
            table = Table(data, repeatRows=1)
            style = [
                ("BACKGROUND", (0,0), (-1,0), colors.grey),
                ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
                ("ALIGN", (0,0), (-1,-1), "CENTER"),
                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0,0), (-1,0), 12),
                ("GRID", (0,0), (-1,-1), 0.5, colors.black),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ]

            risk_col_idx = branch_df.columns.get_loc("Risk Level")
            for i, row in enumerate(branch_df["Risk Level"], start=1):
                color = risk_colors.get(row, colors.white)
                style.append(("BACKGROUND", (risk_col_idx, i), (risk_col_idx, i), color))
                if row == "Medium":
                    style.append(("TEXTCOLOR", (risk_col_idx, i), (risk_col_idx, i), colors.black))
                else:
                    style.append(("TEXTCOLOR", (risk_col_idx, i), (risk_col_idx, i), colors.white))

            table.setStyle(TableStyle(style))
            elements.append(table)
            doc.build(elements)

        st.success("✅ Branch-wise PDFs with Risk Levels & Colors generated Successfully!")

    # -----------------------------
    # Color-coded Risk Table in Streamlit
    # -----------------------------
    st.subheader("📋 Cheque-wise Table with Risk Colors")
    def color_risk(val):
        if val == "High": return "background-color: red; color: white;"
        elif val == "Medium": return "background-color: yellow; color: black;"
        elif val == "Low": return "background-color: green; color: white;"
        elif val == "No Risk": return "background-color: gray; color: white;"
        else: return ""
    st.dataframe(edited_df.style.applymap(color_risk, subset=["Risk Level"]), use_container_width=True)

    # -----------------------------
    # Area-wise Risk Distribution Chart (Tranch 1 only)
    # -----------------------------
    st.subheader("📊 Area-wise Risk Distribution Chart (Tranch 1 only)")
    area_df = edited_df[edited_df["tranch_no"] == 1]
    risk_count = area_df.groupby(["branch_id", "Risk Level"]).size().reset_index(name="count")
    total_per_branch = area_df.groupby("branch_id").size().reset_index(name="total")
    risk_count = risk_count.merge(total_per_branch, on="branch_id")
    risk_count["percent"] = (risk_count["count"]/risk_count["total"])*100
    chart_data = risk_count.pivot(index="branch_id", columns="Risk Level", values="percent").fillna(0)
    st.bar_chart(chart_data, use_container_width=True)

    # -----------------------------
    # Example chart (Pichand branch)
    # -----------------------------
    example_data = pd.DataFrame({
        "branch_id": ["Pichand"]*500,
        "Risk Level": ["High"]*200 + ["Medium"]*100 + ["Low"]*100 + ["No Risk"]*100
    })
    example_count = example_data.groupby(["branch_id", "Risk Level"]).size().reset_index(name="count")
    example_total = example_data.groupby("branch_id").size().reset_index(name="total")
    example_count = example_count.merge(example_total, on="branch_id")
    example_count["percent"] = (example_count["count"]/example_count["total"])*100
    example_chart = example_count.pivot(index="branch_id", columns="Risk Level", values="percent").fillna(0)
    st.subheader("📊 Example Area-wise Risk Chart (Pichand Branch)")
    st.bar_chart(example_chart, use_container_width=True)

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from zipfile import ZipFile

st.header("📑 Cheque-wise Analysis")

# --- File Upload ---
uploaded_cheque = st.file_uploader(
    "Upload Cheque-wise List",
    type=["xlsx", "csv"],
    key="cheque_uploader"
)

if uploaded_cheque:
    # --- Read file ---
    if uploaded_cheque.name.endswith(".csv"):
        cheque_df = pd.read_csv(uploaded_cheque)
    else:
        cheque_df = pd.read_excel(uploaded_cheque)

    # --- Clean column names for consistent access ---
    cheque_df.columns = [str(c).strip() for c in cheque_df.columns]

    # --- Required columns ---
    required_cols = [
        "branch_id", "date_disbursed", "sanction_no",
        "tranch_no", "member_name", "member_cnic"
    ]
    # Keep NumberN if exists
    if any("number" in str(c).strip().lower() for c in cheque_df.columns):
        required_cols.append([c for c in cheque_df.columns if "number" in str(c).strip().lower()][0])

    cheque_df = cheque_df[[col for col in required_cols if col in cheque_df.columns]]

    # --- Name column ---
    cheque_df["Name"] = cheque_df["member_name"]
    cheque_df.drop(columns=["member_name"], inplace=True)

    # --- Date conversion ---
    cheque_df["date_disbursed"] = pd.to_datetime(cheque_df["date_disbursed"], errors="coerce")
    today = datetime.today()
    cheque_df["Months Passed"] = cheque_df["date_disbursed"].apply(
        lambda x: relativedelta(today, x).months + relativedelta(today, x).years * 12 if pd.notnull(x) else ""
    )
    cheque_df["Days Passed"] = cheque_df["date_disbursed"].apply(
        lambda x: (today - x).days if pd.notnull(x) else ""
    )

    # --- Add missing flags ---
    for col in ["House Complete", "Shifted", "Design"]:
        if col not in cheque_df.columns:
            cheque_df[col] = "No" if col in ["House Complete", "Shifted"] else ""

    # --- Load saved flags ---
    if os.path.exists("cheque_flags.csv"):
        saved_flags = pd.read_csv("cheque_flags.csv")
        cheque_df = cheque_df.merge(
            saved_flags,
            on=["sanction_no", "tranch_no"],
            how="left",
            suffixes=("", "_saved")
        )
        for col in ["House Complete", "Shifted", "Design"]:
            if f"{col}_saved" in cheque_df.columns:
                cheque_df[col] = cheque_df[f"{col}_saved"].combine_first(cheque_df[col])
                cheque_df.drop(columns=[f"{col}_saved"], inplace=True)

    # -----------------------------------------
    # 1st Tranch + 2nd Tranch logic
    # -----------------------------------------
    cheque_df["2nd Tranch Status"] = ""

    second_tranch_map = (
        cheque_df[cheque_df["tranch_no"] == 2]
        .groupby("sanction_no")
        .size()
        .to_dict()
    )

    first_tranch_df = cheque_df[cheque_df["tranch_no"] == 1].copy()
    first_tranch_df["2nd Tranch Status"] = first_tranch_df["sanction_no"].apply(
        lambda x: "OK" if x in second_tranch_map else ""
    )

    display_columns = [
        "branch_id", "sanction_no", "tranch_no", "Name", "member_cnic",
        "date_disbursed", "Months Passed", "2nd Tranch Status",
        "House Complete", "Shifted", "Design"
    ]

    # Add NumberN if exists
    number_col_name = None
    for col in first_tranch_df.columns:
        if "number" in str(col).strip().lower():
            number_col_name = col
            display_columns.append(number_col_name)
            break

    display_columns = [c for c in display_columns if c in first_tranch_df.columns]
    editable_df = first_tranch_df[display_columns]

    # --- Editable table for 1st tranche ---
    edited_df = st.data_editor(
        editable_df,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "House Complete": st.column_config.SelectboxColumn(options=["Yes", "No"]),
            "Shifted": st.column_config.SelectboxColumn(options=["Yes", "No"])
        }
    )

    # --- Save updated flags ---
    if st.button("💾 Save Flags", key="save_flags_btn"):
        edited_df[["sanction_no", "tranch_no", "House Complete", "Shifted", "Design"]].to_csv(
            "cheque_flags.csv",
            index=False
        )
        st.success("✅ Flags saved successfully!")

    # --- Branch-wise PDFs ZIP Download Button ---
    if st.button("⬇️ Download All Branch PDFs (ZIP)"):
        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, "w") as zip_file:
            for branch in cheque_df["branch_id"].unique():
                branch_df = edited_df[edited_df["branch_id"] == branch]
                branch_full_df = cheque_df[cheque_df["branch_id"] == branch]

                pdf_buffer = BytesIO()
                doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(A4))
                styles = getSampleStyleSheet()
                elements = []

                elements.append(Paragraph(f"Branch ID: {branch}", styles["Heading1"]))
                elements.append(Spacer(1, 12))

                # --- Correct counts ---
                tranch1 = (branch_df["tranch_no"] == 1).sum()
                tranch2 = (branch_full_df["tranch_no"] == 2).sum()
                pending = tranch1 - tranch2 if tranch1 > tranch2 else 0
                house_complete = branch_df["House Complete"].eq("Yes").sum()
                shifted = branch_df["Shifted"].eq("Yes").sum()
                design_complete = branch_df["Design"].eq("Yes").sum()

                summary_text = f"""
                <b>Summary:</b><br/>
                1st Tranch Cases: {tranch1}<br/>
                2nd Tranch Cases: {tranch2}<br/>
                Pending (1st - 2nd): {pending}<br/>
                House Complete: {house_complete}<br/>
                Shifted: {shifted}<br/>
                Design Complete: {design_complete}<br/>
                """
                elements.append(Paragraph(summary_text, styles["Normal"]))
                elements.append(Spacer(1, 12))

                # --- Prepare table ---
                table_df = branch_df.copy()
                table_df = table_df.drop(columns=["branch_id", "tranch_no"], errors="ignore")

                # Add serial number
                table_df.insert(0, "S.No", range(1, len(table_df) + 1))

                # --- NumberN: keep original Excel data ---
                if number_col_name:
                    table_df["NumberN"] = branch_df[number_col_name].fillna("")
                else:
                    table_df["NumberN"] = ""

                # --- House Complete / Shifted: keep exact value ---
                for col in ["House Complete", "Shifted"]:
                    if col in table_df.columns:
                        table_df[col] = table_df[col].fillna("")

                # --- Create table for PDF ---
                data = [table_df.columns.tolist()] + table_df.values.tolist()
                table = Table(data, repeatRows=1, hAlign="CENTER")
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ]))
                elements.append(table)
                doc.build(elements)
                pdf_buffer.seek(0)

                zip_file.writestr(f"branch_{branch}.pdf", pdf_buffer.getvalue())

        zip_buffer.seek(0)
        st.download_button(
            label="⬇️ Download All Branch PDFs (ZIP)",
            data=zip_buffer.getvalue(),
            file_name="branch_pdfs.zip",
            mime="application/zip"
        )

    # --- Grand Total PDF ---
    if st.button("⬇️ Download Branch-wise PDF Summary with Grand Total", key="pdf_grandtotal_btn"):
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(A4))
        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph("Branch-wise Summary Report", styles["Heading1"]))
        elements.append(Spacer(1, 12))

        summary_list = []
        total_tranch1 = total_tranch2 = total_pending = 0
        total_house = total_shifted = total_design = 0

        for branch in cheque_df["branch_id"].unique():
            branch_df = cheque_df[cheque_df["branch_id"] == branch]
            tranch1 = (branch_df["tranch_no"] == 1).sum()
            tranch2 = (branch_df["tranch_no"] == 2).sum()
            pending = tranch1 - tranch2 if tranch1 > tranch2 else 0
            house_complete = branch_df["House Complete"].eq("Yes").sum()
            shifted = branch_df["Shifted"].eq("Yes").sum()
            design_complete = branch_df["Design"].eq("Yes").sum()

            summary_list.append([
                branch, tranch1, tranch2, pending,
                house_complete, shifted, design_complete
            ])

            total_tranch1 += tranch1
            total_tranch2 += tranch2
            total_pending += pending
            total_house += house_complete
            total_shifted += shifted
            total_design += design_complete

        summary_df = pd.DataFrame(summary_list, columns=[
            "Branch", "1st Tranch", "2nd Tranch", "Pending",
            "House Complete", "Shifted", "Design Complete"
        ])

        summary_df.loc["Grand Total"] = [
            "Grand Total",
            total_tranch1, total_tranch2, total_pending,
            total_house, total_shifted, total_design
        ]

        data = [summary_df.columns.tolist()] + summary_df.astype(str).values.tolist()
        table = Table(data, repeatRows=1, hAlign="CENTER")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#004080")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ]))
        elements.append(table)

        doc.build(elements)
        pdf_buffer.seek(0)

        st.download_button(
            label="⬇️ Download Branch-wise PDF Summary with Grand Total",
            data=pdf_buffer.getvalue(),
            file_name="branch_summary_grandtotal.pdf",
            mime="application/pdf",
            key="download_pdf_summary_grandtotal"
        )
import streamlit as st
import pandas as pd
from fpdf import FPDF
from io import BytesIO
import zipfile

# ---------- PDF Class ----------
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, "Cheque Report", ln=True, align="C")
        self.ln(5)

# ---------- Draw Row Function ----------
def draw_row(pdf, row_data, col_widths, row_height=8):
    """Draw a row of data with proper cell heights"""
    cell_heights = []
    x_start = pdf.get_x()
    y_start = pdf.get_y()

    # First calculate max height
    for i, data in enumerate(row_data):
        x = pdf.get_x()
        y = pdf.get_y()
        pdf.multi_cell(col_widths[i], row_height, str(data), border=0, align="C")
        h = pdf.get_y() - y
        cell_heights.append(h)
        pdf.set_xy(x + col_widths[i], y)

    max_height = max(cell_heights)

    # Now draw border and data again
    pdf.set_xy(x_start, y_start)
    for i, data in enumerate(row_data):
        x = pdf.get_x()
        y = pdf.get_y()
        pdf.multi_cell(col_widths[i], row_height, str(data), border=1, align="C")
        pdf.set_xy(x + col_widths[i], y)
    pdf.set_y(y_start + max_height)

# ---------- Branch Header ----------
def add_branch_header(pdf, branch, headers, col_widths):
    """Add branch name and column headers"""
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 10, f"Branch: {branch}", ln=True, align="L")
    pdf.set_font("Arial", 'B', 9)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 8, header, 1, 0, "C")
    pdf.ln()

# ---------- Streamlit UI ----------
st.title("Cheque Wise Report to PDF (Branch Wise)")

uploaded_file = st.file_uploader("Upload Cheque Data CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Required columns
    required_cols = ["branch_id", "date_disbursed", "cheque_no", "sanction_no", "loan_amount", "group_no", "member_name"]

    # Add missing columns as empty
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    # Keep only required columns
    df = df[required_cols]

    st.write("Data Preview:", df.head())

    # Group by branch
    branch_groups = df.groupby("branch_id")

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        for branch, branch_df in branch_groups:
            pdf = PDF()
            pdf.set_auto_page_break(auto=False, margin=15)
            pdf.add_page()

            # Column headers in exact order
            headers = ["Date Disbursed", "Cheque No", "Sanction No", "Loan Amount", "Group No", "Member Name"]
            col_widths = [25, 25, 25, 25, 20, 35]

            add_branch_header(pdf, branch, headers, col_widths)
            pdf.set_font("Arial", '', 8)

            for _, row in branch_df.iterrows():
                if pdf.get_y() > 260:
                    pdf.add_page()
                    add_branch_header(pdf, branch, headers, col_widths)
                    pdf.set_font("Arial", '', 8)

                row_data = [
                    row["date_disbursed"] if pd.notnull(row["date_disbursed"]) else "",
                    row["cheque_no"],
                    row["sanction_no"],
                    row["loan_amount"],
                    row["group_no"],
                    row["member_name"]
                ]
                draw_row(pdf, row_data, col_widths)

            pdf_bytes = pdf.output(dest="S").encode("latin-1")
            zf.writestr(f"{branch}_cheque_report.pdf", pdf_bytes)

    zip_buffer.seek(0)

    st.download_button(
        label="Download All Branch Reports (ZIP)",
        data=zip_buffer,
        file_name="all_branches_cheque_reports.zip",
        mime="application/zip"
    )
