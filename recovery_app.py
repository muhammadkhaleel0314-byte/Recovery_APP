import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import sqlite3

st.set_page_config(page_title="Login System",)

# ---------- USERS ----------
USERS = {
    "Khaleel": "112345",
    "Baqir@0315": "Baq0ir315",
    "SaneelHaider": "Haider222",
    "Atif Sajjad": "Sajjad222",
    
}

ADMIN_USER = "Khaleel"

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in:

    st.markdown("<h2 style='text-align:center;'>Login</h2>", unsafe_allow_html=True)

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user in USERS and USERS[user] == pwd:
            st.session_state.logged_in = True
            st.session_state.username = user
            st.experimental_rerun()
        else:
            st.error("Invalid Login")

    st.stop()

# ---------- AFTER LOGIN ----------
st.success(f"Welcome {st.session_state.username}")

# ---------- MENU ----------
if st.session_state.username == ADMIN_USER:
    menu = ["Dashboard", "Signup", "Logout"]
else:
    menu = ["Dashboard", "Logout"]

choice = st.sidebar.selectbox("Menu", menu)

# ---------- LOGOUT ----------
if choice == "Logout":
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.experimental_rerun()

# ---------- PAGES ----------
if choice == "Dashboard":
    st.title("Dashboard Screen")

elif choice == "Signup":
    st.title("Signup Page (Only Admin Can See)")



st.markdown("""
    <h1 style='text-align: center; color: White;'>📊 Welcome to Recovery Portal Created By:M.Khaleel</h1>
    <h3 style='text-align: center; color: Yellow;'>Recovery and Overdue Portal</h3>
    <hr style='border-top: 3px solid #bbb;'>
""", unsafe_allow_html=True)
import streamlit as st
import pandas as pd


# =========================
# Merge Function
# =========================
def merge_uploaded_csv(files):
    dfs = []
    for file in files:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


# =========================
# Session State Save
# =========================
if "merged_df" not in st.session_state:
    st.session_state.merged_df = None


# =========================
# Upload
# =========================
files = st.file_uploader(
    "Upload CSV Files",
    type="csv",
    accept_multiple_files=True
)

# =========================
# Merge Button (manual trigger)
# =========================
if st.button("Merge Files"):
    if files:
        st.session_state.merged_df = merge_uploaded_csv(files)
    else:
        st.warning("Upload files first")


# =========================
# Show + Download
# =========================
if st.session_state.merged_df is not None:

    df = st.session_state.merged_df

    st.success(f"Total Rows: {len(df)}")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Merged File",
        data=csv,
        file_name="merged.csv",
        mime="text/csv"
    )

import streamlit as st
import pandas as pd
from io import BytesIO
import os

CACHE_FILE = "sustainability_cache.xlsx"

st.markdown("<h1 style='color:#003366;'>Sustainability Report</h1>", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Options")
project_file = st.sidebar.file_uploader("Upload Project Excel", type=["xlsx"], key="project_upload")
expense_file = st.sidebar.file_uploader("Upload Expenses Excel", type=["xlsx"], key="expense_upload")

# ---------------- LOAD OR CACHE ---------------- #
def load_excel(file):
    return pd.read_excel(file)

# اگر نئی file upload ہو
if project_file is not None:
    df_raw = load_excel(project_file)
    if expense_file is not None:
        df_exp = load_excel(expense_file)
        exp_sum = df_exp.groupby("Branch Code", as_index=False)["Amount"].sum()
        df_raw = df_raw.merge(exp_sum, on="Branch Code", how="left", suffixes=("", "_Expenses"))
        df_raw["Expenses"] = df_raw["Amount_Expenses"].fillna(0)
    else:
        df_raw["Expenses"] = 0
    # save locally for next reopen
    df_raw.to_excel(CACHE_FILE, index=False)
elif os.path.exists(CACHE_FILE):
    # reopen, read cache
    df_raw = pd.read_excel(CACHE_FILE)
else:
    df_raw = pd.DataFrame()

# ---------------- AGGREGATE PER BRANCH ---------------- #
agg_list = []
if not df_raw.empty:
    branch_keys = ["Area", "Branch Name", "Branch Code"]
    grouped = df_raw.groupby(branch_keys, as_index=False)
    for _, g in grouped:
        area = g["Area"].iloc[0]
        branch = g["Branch Name"].iloc[0]
        code = g["Branch Code"].iloc[0]

        project_total = g[~g["Sanction No"].str.contains("D030|D003|D027|D028", na=False)]["Amount"].sum()
        acag_total = g[g["Sanction No"].str.contains("D030", na=False)]["Amount"].sum()
        pmlchs_total = g[g["Sanction No"].str.contains("D003", na=False)]["Amount"].sum()
        pmy_total = g[g["Sanction No"].str.contains("D027|D028", regex=True, na=False)]["Amount"].sum()
        expenses_total = g["Expenses"].dropna().iloc[0] if not g["Expenses"].dropna().empty else 0

        row = {
            "Area": area,
            "Branch": branch,
            "Branch Code": code,
            "Project Disburse": project_total,
            "6% Income": round(project_total * 0.06, 2),
            "ACAG Disburse": acag_total,
            "1% Income": round(acag_total * 0.01, 2),
            "PMLCHS Disburse": pmlchs_total,
            "2% Income": round(pmlchs_total * 0.02, 2),
            "PMY Disburse": pmy_total,
            "3% Income": round(pmy_total * 0.03, 2),
        }
        row["Total Income"] = round(row["6% Income"] + row["1% Income"] + row["2% Income"] + row["3% Income"], 2)
        row["Expenses"] = expenses_total
        row["Difference"] = round(row["Total Income"] - row["Expenses"], 2)
        agg_list.append(row)

df = pd.DataFrame(agg_list)

# ---------------- AREA FILTER ---------------- #
if not df.empty and "Area" in df.columns:
    areas = ["All Areas"] + sorted(df["Area"].dropna().unique())
    selected_area = st.sidebar.selectbox("Select Area", areas)
    if selected_area != "All Areas":
        df_display = df[df["Area"] == selected_area]
    else:
        df_display = df.copy()
else:
    df_display = df.copy()

# ---------------- DISPLAY TABLE ---------------- #
st.subheader("Data Table")
if df_display.empty:
    st.info("Upload Project Excel to view table.")
else:
    st.markdown("<style>td,th{color:white;}</style>", unsafe_allow_html=True)
    st.dataframe(df_display)

# ---------------- DOWNLOAD BUTTON ---------------- #
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="Filtered Report")
    output.seek(0)
    return output

if not df_display.empty:
    excel_data = to_excel(df_display)
    st.sidebar.download_button(
        label=f"⬇️ Download {selected_area} Excel",
        data=excel_data,
        file_name=f"Sustainability_{selected_area}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
# -------------------
# MDP Section with G/P and Grand Total
# -------------------

import streamlit as st
import pandas as pd

from io import BytesIO

# ---------- Fixed Signin Menu ----------

# ---------- MDP Report Expander (Below Signin) ----------
with st.sidebar.expander("📊 MDP Report"):
    st.write("Upload sheets and generate MDP report here")

    # --- File Upload ---
    active_file = st.file_uploader("Upload Active Sheet", type=["xlsx","xls","csv"], key="mdp_active_upload")
    mdp_file = st.file_uploader("Upload MDP Sheet", type=["xlsx","xls","csv"], key="mdp_mdp_upload")

    # --- Placeholders ---
    table_placeholder = st.empty()
    overall_download_placeholder = st.empty()
    area_dropdown_placeholder = st.empty()
    area_download_placeholder = st.empty()

    # --- Show info if files not uploaded ---
    if not active_file or not mdp_file:
        table_placeholder.info("Upload both Active and MDP sheets to generate the MDP report and download options.")

    # --- Main Logic (same as your existing code) ---
    if active_file and mdp_file:
        try:
            active_df = pd.read_csv(active_file) if active_file.name.endswith(".csv") else pd.read_excel(active_file)
            mdp_df = pd.read_csv(mdp_file) if mdp_file.name.endswith(".csv") else pd.read_excel(mdp_file)
        except Exception as e:
            table_placeholder.error(f"Error reading files: {e}")
            st.stop()

        # --- Clean columns ---
        active_df.columns = active_df.columns.str.strip()
        mdp_df.columns = mdp_df.columns.str.strip()

        # --- Pivot Calculation ---
        report_data = []

        for (area, branch), group in mdp_df.groupby(['area_id','branch_id']):
            due_count = len(active_df[active_df['branch_id']==branch])
            amount_sum = group['Due Amount'].sum()
            active_sanctions = active_df[active_df['branch_id']==branch]['Sanction No'].tolist()
            g_by_count = sum([1 for x in active_sanctions if x in group['sanction_no'].values])
            n_a_count = due_count - g_by_count
            p_b = round((g_by_count/due_count)*100,2) if due_count!=0 else 0
            n_p = round((n_a_count/due_count)*100,2) if due_count!=0 else 0
            g_p = p_b  # G/P = same as % of counted borrowers

            report_data.append({
                'Area': area,
                'Branch': branch,
                'Active': '',
                'Due': due_count,
                'Amount': amount_sum,
                'Given/BY': g_by_count,
                'G/P %': g_p,
                'MDP/Box %': p_b,
                'N/A': n_a_count,
                'N/P %': n_p
            })

        report_df = pd.DataFrame(report_data)

        # --- Add Grand Total Row ---
        grand_total = {
            'Area': 'Grand Total',
            'Branch': '',
            'Active': '',
            'Due': report_df['Due'].sum(),
            'Amount': report_df['Amount'].sum(),
            'Given/BY': report_df['Given/BY'].sum(),
            'G/P %': round((report_df['Given/BY'].sum()/report_df['Due'].sum())*100,2) if report_df['Due'].sum()!=0 else 0,
            'MDP/Box %': round((report_df['Given/BY'].sum()/report_df['Due'].sum())*100,2) if report_df['Due'].sum()!=0 else 0,
            'N/A': report_df['N/A'].sum(),
            'N/P %': round((report_df['N/A'].sum()/report_df['Due'].sum())*100,2) if report_df['Due'].sum()!=0 else 0
        }

        report_df = pd.concat([report_df, pd.DataFrame([grand_total])], ignore_index=True)

        # --- Display Table ---
        table_placeholder.dataframe(report_df)

        # --- Excel Helper ---
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='MDP_Report')
            return output.getvalue()

        # --- Overall Download ---
        excel_data = to_excel(report_df)
        overall_download_placeholder.download_button(
            label="📥 Download Overall Report",
            data=excel_data,
            file_name="MDP_Report_Overall.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="mdp_overall_download"
        )

        # --- Area-wise Dropdown & Download ---
        areas = report_df['Area'].unique().tolist()
        areas = [x for x in areas if x!='Grand Total']
        areas.sort()
        areas.insert(0,"All Areas")

        selected_area = area_dropdown_placeholder.selectbox("Select Area", areas, key="mdp_area_dropdown")
        df_to_download = report_df if selected_area=="All Areas" else report_df[report_df['Area']==selected_area]
        excel_data_area = to_excel(df_to_download)

        area_download_placeholder.download_button(
            label=f"📥 Download {selected_area} Report",
            data=excel_data_area,
            file_name=f"MDP_Report_{selected_area}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="mdp_area_download"
        )
import streamlit as st
import pandas as pd
from io import BytesIO

st.markdown("---")
st.subheader("📁 Merge File Upload And Take File With Branch&Area")

# --- File Upload ---
col1, col2 = st.columns(2)
with col1:
    merge_file = st.file_uploader("Upload Merge File (Sanction No)", type=["xlsx","xls","csv"], key="merge_file")
with col2:
    branch_file = st.file_uploader("Upload Branch File (Branch Code)", type=["xlsx","xls","csv"], key="branch_file")

# --- Placeholders ---
merge_table_placeholder = st.empty()
merge_download_placeholder = st.empty()

if merge_file and branch_file:
    try:
        df_merge = pd.read_csv(merge_file) if merge_file.name.endswith(".csv") else pd.read_excel(merge_file)
        df_branch = pd.read_csv(branch_file) if branch_file.name.endswith(".csv") else pd.read_excel(branch_file)
    except Exception as e:
        merge_table_placeholder.error(f"Error reading files: {e}")
        st.stop()

    # --- Clean column names ---
    df_merge.columns = df_merge.columns.str.strip()
    df_branch.columns = df_branch.columns.str.strip()

    # --- Check required columns ---
    if 'sanctionno' not in df_merge.columns:
        st.error("Merge File must have column 'sanctionno'")
        st.stop()
    if 'branch code' not in df_branch.columns or 'branch_name' not in df_branch.columns or 'area_name' not in df_branch.columns:
        st.error("Branch File must have columns 'branch code', 'branch_name', 'area_name'")
        st.stop()

    # --- Ensure columns are string for merge ---
    df_merge['Sanction_Prefix'] = df_merge['sanctionno'].astype(str).str[:4]
    df_branch['branch code'] = df_branch['branch code'].astype(str)

    # --- Merge logic ---
    merged_df = pd.merge(
        df_merge,
        df_branch.rename(columns={'branch code':'Sanction_Prefix'}),
        on='Sanction_Prefix',
        how='left'
    )

    # --- Add Branch Name & Area Name as 3rd and 4th column ---
    if 'branch_name' in merged_df.columns and 'area_name' in merged_df.columns:
        branch_col = merged_df.pop('branch_name')
        area_col = merged_df.pop('area_name')
        merged_df.insert(2, 'Branch Name', branch_col)
        merged_df.insert(3, 'Area Name', area_col)

    # --- Display table ---
    merge_table_placeholder.dataframe(merged_df)

    # --- Download helper ---
    def to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Merged_Report')
        return output.getvalue()

    excel_data = to_excel(merged_df)

    # --- Download button ---
    merge_download_placeholder.download_button(
        label="📥 Download Merged File",
        data=excel_data,
        file_name="Merged_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="merge_download"
    )

else:
    merge_table_placeholder.info("Upload both Merge File and Branch File to generate merged report.")
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

import streamlit as st
import pandas as pd
import io
import zipfile
from fpdf import FPDF
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
import plotly.express as px

st.title("🏦 Recovery & Reports App")

# --------------------
# Uploaders
# --------------------
do_file = st.file_uploader("Upload Do List", type=["xlsx", "xls"])
recovery_file = st.file_uploader("Upload Recovery File", type=["xlsx", "xls"])

# =============================
# SAVE DATA AFTER REFRESH
# =============================
if do_file:
    st.session_state["do_df"] = pd.read_excel(do_file)

if recovery_file:
    st.session_state["recovery_df"] = pd.read_excel(recovery_file)

if "do_df" in st.session_state and "recovery_df" in st.session_state:

    do_df = st.session_state["do_df"]
    recovery_df = st.session_state["recovery_df"]

    do_df.columns = do_df.columns.str.strip()
    recovery_df.columns = recovery_df.columns.str.strip()

    # =============================
    # OVERDUE
    # =============================
    if "Sanction No" not in do_df.columns or "Sanction No" not in recovery_df.columns:
        st.error("Both files must contain 'Sanction No'")
        st.stop()

    overdue_df = do_df[
        ~do_df["Sanction No"].astype(str).isin(
            recovery_df["Sanction No"].astype(str)
        )
    ]

    st.subheader("🕒 Final Overdue List")
    st.dataframe(overdue_df)

    # =============================
    # OVERDUE PDF DOWNLOAD
    # =============================
    if not overdue_df.empty:

        st.subheader("⬇ Download Overdue PDF")

        # AREA FILTER
        if "area_id" in overdue_df.columns:
            areas = sorted(overdue_df["area_id"].astype(str).unique())
            selected_area = st.selectbox("Select Area", ["All Areas"] + areas)

            if selected_area != "All Areas":
                area_df = overdue_df[overdue_df["area_id"].astype(str) == selected_area]
            else:
                area_df = overdue_df
        else:
            area_df = overdue_df
            selected_area = "All"

        # BRANCH FILTER
        branches = sorted(area_df["branch_id"].astype(str).unique())
        selected_branch = st.selectbox("Select Branch", ["All Branches"] + branches)

        if selected_branch != "All Branches":
            branch_df = area_df[area_df["branch_id"].astype(str) == selected_branch]
        else:
            branch_df = area_df

        # PDF GENERATE
        if st.button("Generate PDF"):

            pdf = FPDF()
            pdf.add_page()

            pdf.set_font("Arial","B",14)
            pdf.cell(0,10,"Overdue Report",ln=True)

            pdf.set_font("Arial","",11)
            pdf.cell(0,8,f"Area: {selected_area}",ln=True)
            pdf.cell(0,8,f"Branch: {selected_branch}",ln=True)
            pdf.ln(5)

            # header
            pdf.set_font("Arial","B",10)
            pdf.cell(12,8,"#",1)
            pdf.cell(60,8,"Name",1)
            pdf.cell(60,8,"Sanction No",1)

            if "Mobile No" in branch_df.columns:
                pdf.cell(50,8,"Mobile",1)
            pdf.ln()

            # rows
            pdf.set_font("Arial","",9)
            for i,(_,row) in enumerate(branch_df.iterrows(),1):
                pdf.cell(12,8,str(i),1)
                pdf.cell(60,8,str(row.get("Name",""))[:25],1)
                pdf.cell(60,8,str(row.get("Sanction No","")),1)

                if "Mobile No" in branch_df.columns:
                    pdf.cell(50,8,str(row.get("Mobile No","")),1)
                pdf.ln()

            pdf_bytes = pdf.output(dest="S").encode("latin1")

            st.download_button(
                "⬇ Download PDF",
                pdf_bytes,
                f"Overdue_{selected_area}_{selected_branch}.pdf",
                "application/pdf"
            )

    # =============================
    # RECOVERY SUMMARY
    # =============================
    do_df["Sanction No"]=do_df["Sanction No"].astype(str)
    recovery_df["Sanction No"]=recovery_df["Sanction No"].astype(str)

    if "recovery_date" in recovery_df.columns:
        recovery_df["recovery_date"]=pd.to_datetime(recovery_df["recovery_date"],errors="coerce")
    else:
        recovery_df["recovery_date"]=pd.NaT

    current_month=pd.Timestamp.now().month
    current_year=pd.Timestamp.now().year

    recovery_this_month=recovery_df[
        (recovery_df["recovery_date"].dt.month==current_month) &
        (recovery_df["recovery_date"].dt.year==current_year)
    ]

    recovered=recovery_this_month[
        recovery_this_month["Sanction No"].isin(do_df["Sanction No"])
    ]

    if "branch_id" not in do_df.columns:
        do_df["branch_id"]="Unknown"

    if "branch_id" not in recovery_df.columns:
        recovery_df["branch_id"]="Unknown"

    due=do_df.groupby("branch_id")["Sanction No"].count().reset_index(name="total_due")
    rec=recovered.groupby("branch_id")["Sanction No"].count().reset_index(name="recovered")

    summary=due.merge(rec,on="branch_id",how="left").fillna(0)
    summary["remaining"]=summary["total_due"]-summary["recovered"]
    summary["percent"]=(summary["recovered"]/summary["total_due"])*100

    st.subheader("📊 Branch Recovery Summary")
    st.dataframe(summary)

    fig=px.bar(summary,x="branch_id",y="percent",text=summary["percent"].round(1))
    st.plotly_chart(fig,use_container_width=True)

    st.write("Total Due:",len(do_df))
    st.write("Recovered This Month:",len(recovered))

# =============================
# TERABYTE SECTION (UNCHANGED)
# =============================
terabyte_file = st.file_uploader("Upload Terabyte Excel", type=["xlsx","xls"])

if terabyte_file:
    df=pd.read_excel(terabyte_file)

    req=["Sanction No","Recovery Date","Receipt No","Credit Amount","Branch Code"]
    missing=[c for c in req if c not in df.columns]

    if missing:
        st.error(f"Missing columns: {missing}")
    else:
        df["Recovery Date"]=pd.to_datetime(df["Recovery Date"]).dt.date
        df.insert(0,"Sr#",range(1,len(df)+1))

        st.dataframe(df.head())

        branches=df["Branch Code"].unique()

        for b in branches:
            branch_df=df[df["Branch Code"]==b]

            buf=io.BytesIO()
            doc=SimpleDocTemplate(buf,pagesize=letter)
            styles=getSampleStyleSheet()
            elements=[Paragraph(f"Branch {b}",styles["Heading1"]),Spacer(1,12)]

            table_data=[list(branch_df.columns)]+branch_df.values.tolist()
            table=Table(table_data)
            table.setStyle(TableStyle([
                ("GRID",(0,0),(-1,-1),1,colors.black)
            ]))
            elements.append(table)
            doc.build(elements)
            buf.seek(0)

            st.download_button(
                f"Download Branch {b} PDF",
                buf.getvalue(),
                f"branch_{b}.pdf",
                "application/pdf"
            )
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
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from zipfile import ZipFile

st.header("📑 Cheque-wise Analysis")

uploaded_cheque = st.file_uploader("Upload Cheque-wise List", type=["xlsx", "csv"])

if uploaded_cheque:

    if uploaded_cheque.name.endswith(".csv"):
        cheque_df = pd.read_csv(uploaded_cheque)
    else:
        cheque_df = pd.read_excel(uploaded_cheque)

    cheque_df.columns = [str(c).strip() for c in cheque_df.columns]

    required_cols = ["branch_id","date_disbursed","sanction_no","tranch_no","member_name","member_cnic"]
    cheque_df = cheque_df[[c for c in required_cols if c in cheque_df.columns]]

    cheque_df["Name"] = cheque_df["member_name"]
    cheque_df.drop(columns=["member_name"], inplace=True)

    cheque_df["date_disbursed"] = pd.to_datetime(cheque_df["date_disbursed"], errors="coerce")

    today = datetime.today()

    cheque_df["Months Passed"] = cheque_df["date_disbursed"].apply(
        lambda x: relativedelta(today, x).months + relativedelta(today, x).years*12 if pd.notnull(x) else ""
    )

    cheque_df["Days Passed"] = cheque_df["date_disbursed"].apply(
        lambda x: (today-x).days if pd.notnull(x) else ""
    )

    for col in ["House Complete","Shifted","Design"]:
        if col not in cheque_df.columns:
            cheque_df[col] = ""

    cheque_df["2nd Tranch Status"] = ""

    second_map = cheque_df[cheque_df["tranch_no"]==2].groupby("sanction_no").size().to_dict()

    first_df = cheque_df[cheque_df["tranch_no"]==1].copy()
    first_df["2nd Tranch Status"] = first_df["sanction_no"].apply(lambda x:"OK" if x in second_map else "")

    display_cols = ["branch_id","sanction_no","tranch_no","Name","member_cnic",
                    "date_disbursed","Months Passed","2nd Tranch Status",
                    "House Complete","Shifted","Design"]

    editable_df = first_df[display_cols]

    # -------- Editable Table --------
    edited_df = st.experimental_data_editor(editable_df, use_container_width=True)

    # -------- CSV Download --------
    csv_data = edited_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Edited CSV",
        csv_data,
        "cheque_analysis.csv",
        "text/csv"
    )

    # -------- Save Flags --------
    if st.button("💾 Save Flags"):
        edited_df[["sanction_no","tranch_no","House Complete","Shifted","Design"]].to_csv(
            "cheque_flags.csv", index=False
        )
        st.success("Saved")

    # -------- ZIP PDFs --------
    if st.button("⬇️ Download All Branch PDFs (ZIP)"):

        zip_buffer = BytesIO()

        with ZipFile(zip_buffer,"w") as zipf:

            for branch in edited_df["branch_id"].unique():

                bdf = edited_df[edited_df["branch_id"]==branch]

                pdf = BytesIO()
                doc = SimpleDocTemplate(pdf, pagesize=landscape(A4))
                styles = getSampleStyleSheet()
                elements=[]

                elements.append(Paragraph(f"Branch {branch}",styles["Heading1"]))
                elements.append(Spacer(1,10))

                table_df = bdf.drop(columns=["branch_id","tranch_no"],errors="ignore")
                table_df.insert(0,"S.No",range(1,len(table_df)+1))

                data=[table_df.columns.tolist()]+table_df.astype(str).values.tolist()

                table=Table(data,repeatRows=1)
                table.setStyle(TableStyle([
                    ("GRID",(0,0),(-1,-1),0.5,colors.black),
                    ("ALIGN",(0,0),(-1,-1),"CENTER")
                ]))

                elements.append(table)
                doc.build(elements)
                pdf.seek(0)

                zipf.writestr(f"branch_{branch}.pdf",pdf.getvalue())

        zip_buffer.seek(0)

        st.download_button(
            "Download ZIP",
            zip_buffer.getvalue(),
            "branches.zip",
            "application/zip"
        )
import streamlit as st
import pandas as pd
from fpdf import FPDF

st.title("Loan Disbursement PDF Generator (Branchwise)")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

# ---------------------- Safe Functions ----------------------
def safe(val):
    try:
        if pd.isna(val):
            return ""
        return str(val)
    except:
        return ""

# ---------------------- PDF Class ----------------------
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 8, "Loan Disbursement Report", ln=True, align="C")
        self.ln(3)

# ---------------------- MAIN ----------------------
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Fix column spellings
    df.rename(columns={
        "date_disbursed": "date_disburse",
        "date_of_disbursement": "date_disburse",
        "tranch_no": "tranch",
        "grouo_no": "group_no",
    }, inplace=True)

    # Required Columns
    required_cols = [
        "branch_id", "member_name", "member_cnic", "loan_amount",
        "tranch", "cheque_no", "sanction_no",
        "group_no", "date_disburse"
    ]

    # Check Missing Columns
    missing = [c for c in required_cols if c not in df.columns]

    if missing:
        st.error(f"Missing columns: {missing}")
        st.stop()

    # ---------------------- Branch Dropdown ----------------------
    branches = df["branch_id"].unique()
    selected_branch = st.selectbox("Select Branch", options=branches)

    # Filter dataframe for selected branch
    br_df = df[df["branch_id"] == selected_branch]
    st.dataframe(br_df)

    # ---------------------- Download PDF ----------------------
    if st.button(f"Download PDF for Branch {selected_branch}"):

        pdf = PDF(orientation="L", unit="mm", format="A4")  # LANDSCAPE
        pdf.set_auto_page_break(auto=True, margin=10)
        pdf.add_page()

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, f"Branch: {selected_branch}", ln=True, align="C")
        pdf.ln(3)

        # ---------------------- TABLE HEADER ----------------------
        headers = [
            "Date Disburse", "Sanction No", "Tranch", "Cheque No",
            "Loan Amount", "Group No", "Member Name", "CNIC"
        ]
        col_widths = [30, 35, 15, 40, 30, 30, 55, 45]

        pdf.set_fill_color(200, 200, 200)
        pdf.set_font("Arial", 'B', 9)
        for i, h in enumerate(headers):
            pdf.cell(col_widths[i], 8, h, border=1, align="C", fill=True)
        pdf.ln()

        # ---------------------- TABLE ROWS ----------------------
        fill = False
        for _, row in br_df.iterrows():
            pdf.set_fill_color(235, 245, 255) if fill else pdf.set_fill_color(255, 255, 255)
            pdf.set_font("Arial", '', 9)
            pdf.cell(col_widths[0], 7, safe(row["date_disburse"]), border=1, fill=True)
            pdf.cell(col_widths[1], 7, safe(row["sanction_no"]), border=1, fill=True)
            pdf.cell(col_widths[2], 7, safe(row["tranch"]), border=1, fill=True)
            pdf.cell(col_widths[3], 7, safe(row["cheque_no"]), border=1, fill=True)
            pdf.cell(col_widths[4], 7, safe(row["loan_amount"]), border=1, fill=True)
            pdf.cell(col_widths[5], 7, safe(row["group_no"]), border=1, fill=True)
            pdf.cell(col_widths[6], 7, safe(row["member_name"]), border=1, fill=True)
            pdf.cell(col_widths[7], 7, safe(row["member_cnic"]), border=1, fill=True)
            pdf.ln()
            fill = not fill

        # Export PDF
        pdf_bytes = pdf.output(dest="S").encode("latin-1")
        st.download_button(
            label=f"Download {selected_branch} PDF",
            data=pdf_bytes,
            file_name=f"{selected_branch}_Loan_Disbursement.pdf",
            mime="application/pdf"
        )
import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import os

# ---------------- PAGE CONFIG ----------------

st.title("Recovery Date Range Summary")

# ---------------- Local storage folder ----------------
LOCAL_FOLDER = "data"
LOCAL_FILE = os.path.join(LOCAL_FOLDER, "recovery.xlsx")
os.makedirs(LOCAL_FOLDER, exist_ok=True)

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader("Upload Recovery Excel / CSV", type=["xlsx", "csv"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.session_state["df"] = df
        df.to_excel(LOCAL_FILE, index=False)
        st.success("File uploaded and saved locally!")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

# ---------------- Load from session or local file ----------------
elif "df" in st.session_state:
    df = st.session_state["df"]
    st.info("Using previously uploaded file from session.")
elif os.path.exists(LOCAL_FILE):
    try:
        df = pd.read_excel(LOCAL_FILE)
        st.session_state["df"] = df
        st.info("Loaded previously saved file from local storage.")
    except Exception as e:
        st.error(f"Error loading local file: {e}")
        st.stop()
else:
    st.info("Please upload a recovery file to proceed.")
    st.stop()

# ---------------- Column Selection ----------------
st.subheader("Available Columns")
st.write(list(df.columns))

date_col = st.selectbox("Select Date Column", df.columns)
branch_col = st.selectbox("Select Branch Column (branch_id)", df.columns)
area_col = None
if 'area_id' in df.columns:
    area_col = 'area_id'

# ---------------- Convert Date & Create Day/Range ----------------
df[date_col] = pd.to_datetime(df[date_col].astype(str).str.strip(), errors='coerce')
df = df.dropna(subset=[date_col, branch_col])
df["Day"] = df[date_col].dt.day
df = df[df["Day"].notna()]

df["Range"] = pd.cut(df["Day"], bins=[0,10,20,31], labels=["1-10","11-20","21-31"])
if df["Range"].isna().all():
    st.error("Date column format not recognized.")
    st.stop()

# ---------------- Pivot Table ----------------
try:
    pivot = pd.pivot_table(
        df,
        index=[branch_col],
        columns="Range",
        aggfunc="size",
        fill_value=0
    )
except KeyError as e:
    st.error(f"Pivot error: {e}")
    st.stop()

# Ensure columns exist
for c in ["1-10","11-20","21-31"]:
    if c not in pivot.columns:
        pivot[c] = 0

pivot["Total"] = pivot[["1-10","11-20","21-31"]].sum(axis=1)
pivot["1-10 %"] = (pivot["1-10"] / pivot["Total"] * 100).round(2)
pivot["11-20 %"] = (pivot["11-20"] / pivot["Total"] * 100).round(2)
pivot["21-31 %"] = (pivot["21-31"] / pivot["Total"] * 100).round(2)

pivot.rename(columns={
    "1-10": "Recovery 1-10",
    "11-20": "Recovery 11-20",
    "21-31": "Recovery 21-31"
}, inplace=True)

result_df = pivot.reset_index()

# ---------------- Add Area column BEFORE Branch ----------------
if area_col:
    branch_area_df = df[[branch_col, area_col]].drop_duplicates()
    result_df = result_df.merge(branch_area_df, on=branch_col, how='left')
    cols = result_df.columns.tolist()
    branch_idx = cols.index(branch_col)
    cols.insert(branch_idx, cols.pop(cols.index(area_col)))
    result_df = result_df[cols]

# ---------------- Grand Total Row ----------------
numeric_cols = ["Recovery 1-10","Recovery 11-20","Recovery 21-31","Total"]
grand_total_counts = result_df[numeric_cols].sum()
grand_total_percent = (grand_total_counts[["Recovery 1-10","Recovery 11-20","Recovery 21-31"]] / grand_total_counts["Total"] * 100).round(2)

grand_values = {}
for col in result_df.columns:
    if col == branch_col:
        grand_values[col] = "Grand Total"
    elif col == area_col:
        grand_values[col] = ""
    elif col in numeric_cols:
        grand_values[col] = grand_total_counts[col]
    elif col in ["1-10 %","11-20 %","21-31 %"]:
        pct_map = {"1-10 %":"Recovery 1-10","11-20 %":"Recovery 11-20","21-31 %":"Recovery 21-31"}
        grand_values[col] = grand_total_percent[pct_map[col]]
    else:
        grand_values[col] = ""

result_df = pd.concat([result_df, pd.DataFrame([grand_values])], ignore_index=True)

# ---------------- Display Table ----------------
st.subheader("Branch Wise Recovery Summary")
st.dataframe(result_df)

# ---------------- CSV Download ----------------
csv = result_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name="recovery_summary.csv",
    mime="text/csv"
)

# ---------------- PDF Download ----------------
buffer = BytesIO()
doc = SimpleDocTemplate(buffer, pagesize=A4)
table_data = [result_df.columns.tolist()] + result_df.values.tolist()

table = Table(table_data)
style = TableStyle([
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,0), 6),
])
table.setStyle(style)
doc.build([table])
pdf_bytes = buffer.getvalue()
buffer.close()

st.download_button(
    label="⬇ Download PDF",
    data=pdf_bytes,
    file_name="recovery_summary.pdf",
    mime="application/pdf"
)





