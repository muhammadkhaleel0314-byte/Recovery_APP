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
    "Khaleel": "12345",
    "Baqir@0315": "Baqir315",
    "SaneelHaider": "Haider222"
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
from io import BytesIO

st.set_page_config(layout="wide")
st.title("Target vs Achievement MIS")

# ---------------- SESSION STATE ---------------- #
if "mis_data" not in st.session_state:
    st.session_state.mis_data = {
        "projects": ["ACAG","AIM PF","PM-ALS & YBLS","PSPA","PM-LCH","Akhuwat","KLP"],
        "target": [],
        "achievement": []
    }

# ---------------- UPLOAD TARGET SHEET ---------------- #
target_file = st.sidebar.file_uploader("Upload Target Sheet (Excel/CSV)", type=["xlsx","csv"])
if target_file:
    try:
        if target_file.name.endswith(".csv"):
            df_target = pd.read_csv(target_file)
        else:
            df_target = pd.read_excel(target_file)
        st.session_state.mis_data["target"] = []
        # Auto populate target rows from sheet
        for _, row in df_target.iterrows():
            area = str(row.get("Area","")).strip()
            branch = str(row.get("Branch Name","")).strip()
            code = str(row.get("Branch Code","")).strip()
            values = []
            for p in st.session_state.mis_data["projects"]:
                # sum cases and amounts for each project
                proj_rows = df_target[(df_target["Branch Code"]==code) & (df_target["Project Name"]==p)]
                c_sum = len(proj_rows)
                a_sum = proj_rows["Amount"].sum() if not proj_rows.empty else 0
                values.append({"c":c_sum,"a":a_sum})
            st.session_state.mis_data["target"].append({
                "area": area,
                "branch": branch,
                "code": code,
                "values": values
            })
    except Exception as e:
        st.error(f"Error reading target file: {e}")

# ---------------- UPLOAD ACHIEVEMENT ---------------- #
ach_file = st.sidebar.file_uploader("Upload Achievement Sheet (Excel/CSV)", type=["xlsx","csv"])
if ach_file:
    try:
        if ach_file.name.endswith(".csv"):
            df_ach = pd.read_csv(ach_file)
        else:
            df_ach = pd.read_excel(ach_file)
        st.session_state.mis_data["achievement"] = []
        for _, row in df_ach.iterrows():
            area = str(row.get("Area","")).strip()
            branch = str(row.get("Branch Name","")).strip()
            values = []
            for p in st.session_state.mis_data["projects"]:
                proj_rows = df_ach[(df_ach["Branch Name"]==branch) & (df_ach["Project Name"]==p)]
                c_sum = len(proj_rows)
                a_sum = proj_rows["Amount"].sum() if not proj_rows.empty else 0
                values.append({"c":c_sum,"a":a_sum})
            st.session_state.mis_data["achievement"].append({
                "area": area,
                "branch": branch,
                "values": values
            })
    except Exception as e:
        st.error(f"Error reading achievement file: {e}")

# ---------------- REMOVE TARGET ROW ---------------- #
def remove_row(idx):
    st.session_state.mis_data["target"].pop(idx)

# ---------------- RENDER TABLE ---------------- #
def render_table():
    projects = st.session_state.mis_data["projects"]
    targets = st.session_state.mis_data["target"]
    achievements = st.session_state.mis_data["achievement"]

    # Filter area if selected
    areas = ["All Areas"] + sorted(list({t["area"] for t in targets}))
    selected_area = st.sidebar.selectbox("Filter Area", areas)
    display_targets = [t for t in targets if t["area"]==selected_area or selected_area=="All Areas"]

    html = "<table style='width:100%;border-collapse:collapse;text-align:center;'>"
    html += "<tr style='background:#2e7d32;color:white;'><th>Area</th><th>Branch</th>"
    for p in projects:
        html += f"<th colspan='2'>{p}</th>"
    html += "<th>Total</th><th>Action</th></tr>"
    html += "<tr style='background:#2e7d32;color:white;'><th></th><th></th>"
    for _ in projects:
        html += "<th>Cases</th><th>Amount</th>"
    html += "<th></th><th></th></tr>"

    # Target Rows
    for i, t in enumerate(display_targets):
        row_html = f"<tr style='color:white;background:#3e7d32'><td>{t['area']}</td><td>{t['branch']}</td>"
        tc_total = 0
        ta_total = 0
        for v in t["values"]:
            tc_total += v["c"]
            ta_total += v["a"]
            row_html += f"<td>{v['c']}</td><td>{v['a']}</td>"
        row_html += f"<td>{tc_total}|{ta_total}</td>"
        row_html += f"<td><button onclick=''>🗑 Remove</button></td>"
        row_html += "</tr>"
        html += row_html

    # Achievement Rows
    html += f"<tr style='background:#9bbb59;color:white;'><td colspan='{2+len(projects)*2+2}'>ACHIEVEMENT</td></tr>"
    for t in display_targets:
        a = next((x for x in achievements if x["branch"]==t["branch"] and x["area"]==t["area"]), None)
        row_html = f"<tr style='color:white;background:#4b7d42'><td>{t['area']}</td><td>{t['branch']}</td>"
        tc_total = 0
        ta_total = 0
        for i,_ in enumerate(t["values"]):
            c = a["values"][i]["c"] if a else 0
            am = a["values"][i]["a"] if a else 0
            tc_total += c
            ta_total += am
            row_html += f"<td>{c}</td><td>{am}</td>"
        row_html += f"<td>{tc_total}|{ta_total}</td><td></td></tr>"
        html += row_html

    # Variance Rows
    html += f"<tr style='background:#f2a65a;color:white;'><td colspan='{2+len(projects)*2+2}'>VARIANCE</td></tr>"
    for t in display_targets:
        a = next((x for x in achievements if x["branch"]==t["branch"] and x["area"]==t["area"]), None)
        row_html = f"<tr style='color:white;background:#3a7d42'><td>{t['area']}</td><td>{t['branch']}</td>"
        tc_total=0; ta_total=0
        for i,v in enumerate(t["values"]):
            c = v["c"] - (a["values"][i]["c"] if a else 0)
            am = v["a"] - (a["values"][i]["a"] if a else 0)
            tc_total+=c; ta_total+=am
            row_html += f"<td>{c}</td><td>{am}</td>"
        row_html += f"<td>{tc_total}|{ta_total}</td><td></td></tr>"
        html += row_html

    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)

st.subheader("MIS Table")
render_table()

# ---------------- DOWNLOAD EXCEL ---------------- #
def download_excel():
    projects = st.session_state.mis_data["projects"]
    targets = st.session_state.mis_data["target"]
    achievements = st.session_state.mis_data["achievement"]
    aoa = []

    for sec in ["TARGET","ACHIEVEMENT","VARIANCE"]:
        aoa.append([sec])
        h1=["Area","Branch"]; h2=["",""]
        for p in projects: h1.extend([p,""]); h2.extend(["Cases","Amount"])
        aoa.append(h1); aoa.append(h2)
        for t in targets:
            a = next((x for x in achievements if x["area"]==t["area"] and x["branch"]==t["branch"]), None)
            row=[t["area"],t["branch"]]
            tc=0; ta=0
            for i,v in enumerate(t["values"]):
                if sec=="TARGET": c=v["c"]; am=v["a"]
                elif sec=="ACHIEVEMENT": c=a["values"][i]["c"] if a else 0; am=a["values"][i]["a"] if a else 0
                else: c=v["c"]-(a["values"][i]["c"] if a else 0); am=v["a"]-(a["values"][i]["a"] if a else 0)
                tc+=c; ta+=am
                row.extend([c,am])
            row.append(f"{tc}|{ta}")
            aoa.append(row)
        aoa.append([])

    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        pd.DataFrame(aoa).to_excel(writer, index=False, header=False)
    output.seek(0)
    return output

if st.button("⬇ Download Excel"):
    excel_data = download_excel()
    st.download_button("Download MIS Excel", data=excel_data,
                       file_name="Target_vs_Achievement.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
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
                Amount_Sum=("Credit amount", "sum")
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
                    pdf.cell(40, 8, "amount", 1, 0, "C")
                    pdf.cell(60, 8, "Name", 1, 0, "C")
                    pdf.cell(40, 8, "Sanction No", 1, 1, "C")

                    pdf.set_font("Arial", "", 9)
                    total_amount = 0.0
                    for i, (_, row) in enumerate(branch_data.iterrows(), start=1):
                        pdf.cell(12, 8, str(i), 1, 0, "C")
                        pdf.cell(50, 8, str(row.get("Date", ""))[:10], 1, 0, "C")
                        pdf.cell(40, 8, str(row.get("amount", "")), 1, 0, "R")
                        pdf.cell(60, 8, str(row.get("Name", ""))[:25], 1, 0, "L")
                        pdf.cell(40, 8, str(row.get("Sanction No", "")), 1, 1, "C")
                        try:
                            total_amount += float(row.get("amount", 0) if row.get("amount", 0) != "" else 0)
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
CACHE_FILE = "Recovery Date Range Summary_cache.xlsx"

st.title("Recovery Date Range Summary")

# ---------------- Local storage folder ----------------
LOCAL_FILE = "data/recovery.xlsx"
os.makedirs("data", exist_ok=True)

# ---------------- File Upload ----------------
uploaded = st.file_uploader("Upload Recovery Excel / CSV", type=["xlsx", "csv"])

# --- If uploaded, save locally and store in session_state ---
if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)

    st.session_state["df"] = df
    df.to_excel(LOCAL_FILE, index=False)
    st.success("File uploaded and saved locally!")

# --- If no upload, check session_state or local file ---
elif "df" in st.session_state:
    df = st.session_state["df"]
    st.info("Using previously uploaded file from session.")
elif os.path.exists(LOCAL_FILE):
    df = pd.read_excel(LOCAL_FILE)
    st.session_state["df"] = df
    st.info("Loaded previously uploaded file from local storage.")
else:
    st.info("Please upload recovery file.")
    st.stop()

# ---------------- Column Selection ----------------
st.subheader("Available Columns")
st.write(list(df.columns))

date_col = st.selectbox("Select Date Column", df.columns)
branch_col = st.selectbox("Select Branch Column (branch_id)", df.columns)
area_col = None
if 'area_id' in df.columns:
    area_col = 'area_id'

# ---------------- Convert Date ----------------
df[date_col] = pd.to_datetime(
    df[date_col].astype(str).str.strip(),
    format="%Y-%b-%d",
    errors="coerce"
)
df = df.dropna(subset=[date_col, branch_col])
df["Day"] = df[date_col].dt.day
df = df[df["Day"].notna()]

df["Range"] = pd.cut(
    df["Day"],
    bins=[0,10,20,31],
    labels=["1-10","11-20","21-31"]
)
if df["Range"].isna().all():
    st.error("Date column sahi format me nahi.")
    st.stop()

# ---------------- Pivot Table ----------------
pivot = pd.pivot_table(
    df,
    index=[branch_col],
    columns="Range",
    aggfunc="size",
    fill_value=0
)

# Ensure columns exist
for c in ["1-10","11-20","21-31"]:
    if c not in pivot.columns:
        pivot[c] = 0

pivot["Total"] = pivot[["1-10","11-20","21-31"]].sum(axis=1)

# Percentages
pivot["1-10 %"] = (pivot["1-10"] / pivot["Total"] * 100).round(2)
pivot["11-20 %"] = (pivot["11-20"] / pivot["Total"] * 100).round(2)
pivot["21-31 %"] = (pivot["21-31"] / pivot["Total"] * 100).round(2)

# Rename for readability
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
    # Move Area column before Branch column
    cols = result_df.columns.tolist()
    branch_idx = cols.index(branch_col)
    cols.insert(branch_idx, cols.pop(cols.index(area_col)))
    result_df = result_df[cols]

# ---------------- Grand Total Row ----------------
numeric_cols = ["Recovery 1-10","Recovery 11-20","Recovery 21-31","Total"]
# Sum numeric counts
grand_total_counts = result_df[numeric_cols].sum()
# Calculate percentages for Grand Total
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
        # Map numeric col to percentage col
        pct_map = {"1-10 %":"Recovery 1-10","11-20 %":"Recovery 11-20","21-31 %":"Recovery 21-31"}
        grand_values[col] = grand_total_percent[pct_map[col]]
    else:
        grand_values[col] = ""

result_df = pd.concat([result_df, pd.DataFrame([grand_values])], ignore_index=True)

# ---------------- Show Table ----------------
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

# Table data
table_data = [result_df.columns.tolist()] + result_df.values.tolist()

# Create Table with style
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
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(layout="wide")
st.title("Target vs Achievement MIS")

# ---------------- SESSION STATE ---------------- #
if "mis_data" not in st.session_state:
    st.session_state.mis_data = {
        "projects": ["ACAG","AIM PF","PM-ALS & YBLS","PSPA","PM-LCH","Akhuwat","KLP"],
        "target": [],
        "achievement": []
    }

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Options")
target_file = st.sidebar.file_uploader("Upload Target Excel/CSV", type=["xlsx","xls","csv"])
achievement_file = st.sidebar.file_uploader("Upload Achievement Excel/CSV", type=["xlsx","xls","csv"])

# ---------------- HELPER: READ EXCEL/CSV ---------------- #
def read_file(f):
    if f.name.endswith(".csv"):
        return pd.read_csv(f)
    else:
        return pd.read_excel(f)

# ---------------- UPLOAD ACHIEVEMENT ---------------- #
if achievement_file:
    ach_df = read_file(achievement_file)
    ach_df.columns = ach_df.columns.str.strip()
    group = {}
    for _, row in ach_df.iterrows():
        area = str(row.get("Area","")).strip()
        branch = str(row.get("Branch","")).strip()
        proj = row.get("Project")
        amount = row.get("Amount",0)

        if proj is None or not area or not branch:
            continue

        # Project mapping
        if "ALS" in str(proj) or "YBLS" in str(proj):
            proj = "PM-ALS & YBLS"
        elif "KLP" in str(proj):
            proj = "KLP"
        key = f"{area.lower()}|{branch.lower()}|{proj}"

        if key not in group:
            group[key] = {"area":area,"branch":branch,"proj":proj,"c":0,"a":0,"count":0}
        group[key]["a"] += amount
        group[key]["count"] += 1

    # Merge into session_state
    for g in group.values():
        idx = next((i for i,x in enumerate(st.session_state.mis_data["achievement"])
                    if x["area"].lower()==g["area"].lower() and x["branch"].lower()==g["branch"].lower()), -1)
        if idx<0:
            st.session_state.mis_data["achievement"].append({
                "area": g["area"], "branch": g["branch"],
                "values":[{"c":0,"a":0} for _ in st.session_state.mis_data["projects"]]
            })
            idx = len(st.session_state.mis_data["achievement"])-1
        pi = st.session_state.mis_data["projects"].index(g["proj"]) if g["proj"] in st.session_state.mis_data["projects"] else -1
        if pi>=0:
            st.session_state.mis_data["achievement"][idx]["values"][pi]["c"] = g["count"]
            st.session_state.mis_data["achievement"][idx]["values"][pi]["a"] = g["a"]

# ---------------- ADD TARGET ROW ---------------- #
if st.sidebar.button("➕ Add Target Row"):
    st.session_state.mis_data["target"].append({
        "area":"", "branch":"", "values":[{"c":0,"a":0} for _ in st.session_state.mis_data["projects"]]
    })

# ---------------- AREA FILTER ---------------- #
areas = list(set([r["area"] for r in st.session_state.mis_data["target"]]))
areas.sort()
areas.insert(0,"All Areas")
selected_area = st.sidebar.selectbox("Select Area", areas)

# ---------------- DISPLAY TABLE ---------------- #
def render_table():
    projects = st.session_state.mis_data["projects"]
    targets = st.session_state.mis_data["target"]
    achievements = st.session_state.mis_data["achievement"]

    if selected_area!="All Areas":
        targets = [r for r in targets if r["area"]==selected_area]

    # Header
    header1 = ["Area","Branch"] + [p for p in projects for _ in (0,1)] + ["Total"]
    header2 = ["",""] + ["Cases","Amount"]*len(projects) + [""]

    table_html = "<table style='width:100%;border-collapse:collapse;text-align:center;'>"
    table_html += "<tr style='background:#2e7d32;color:white;'>"+ "".join([f"<th>{h}</th>" for h in header1]) + "</tr>"
    table_html += "<tr style='background:#2e7d32;color:white;'>"+ "".join([f"<th>{h}</th>" for h in header2]) + "</tr>"

    # Target Rows
    for t in targets:
        row_html = f"<tr style='color:white;background:#3e7d32'><td>{t['area']}</td><td>{t['branch']}</td>"
        tc_total = 0
        ta_total = 0
        for i,v in enumerate(t["values"]):
            tc_total += v["c"]
            ta_total += v["a"]
            row_html += f"<td>{v['c']}</td><td>{v['a']}</td>"
        row_html += f"<td>{tc_total}|{ta_total}</td></tr>"
        table_html += row_html

    # Achievement Rows
    table_html += "<tr style='background:#9bbb59;color:white;'><td colspan='{0}'>ACHIEVEMENT</td></tr>".format(len(header1))
    for t in targets:
        a = next((x for x in achievements if x["area"].lower()==t["area"].lower() and x["branch"].lower()==t["branch"].lower()), None)
        row_html = f"<tr style='color:white;background:#4b7d42'><td>{t['area']}</td><td>{t['branch']}</td>"
        tc_total = 0
        ta_total = 0
        for i,_ in enumerate(t["values"]):
            c = a["values"][i]["c"] if a else 0
            am = a["values"][i]["a"] if a else 0
            tc_total += c
            ta_total += am
            row_html += f"<td>{c}</td><td>{am}</td>"
        row_html += f"<td>{tc_total}|{ta_total}</td></tr>"
        table_html += row_html

    # Variance
    table_html += "<tr style='background:#f2a65a;color:white;'><td colspan='{0}'>VARIANCE</td></tr>".format(len(header1))
    for t in targets:
        a = next((x for x in achievements if x["area"].lower()==t["area"].lower() and x["branch"].lower()==t["branch"].lower()), None)
        row_html = f"<tr style='color:white;background:#3a7d42'><td>{t['area']}</td><td>{t['branch']}</td>"
        tc_total = 0
        ta_total = 0
        for i,v in enumerate(t["values"]):
            c = v["c"] - (a["values"][i]["c"] if a else 0)
            am = v["a"] - (a["values"][i]["a"] if a else 0)
            tc_total += c
            ta_total += am
            row_html += f"<td>{c}</td><td>{am}</td>"
        row_html += f"<td>{tc_total}|{ta_total}</td></tr>"
        table_html += row_html

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)

st.subheader("MIS Table")
render_table()

# ---------------- DOWNLOAD ---------------- #
def to_excel():
    projects = st.session_state.mis_data["projects"]
    targets = st.session_state.mis_data["target"]
    achievements = st.session_state.mis_data["achievement"]

    aoa=[]
    # Header
    header1=["Area","Branch"]+[p for p in projects for _ in (0,1)]+["Total"]
    header2=["",""]+["Cases","Amount"]*len(projects)+[""]
    aoa.append(header1)
    aoa.append(header2)

    for sec_name,sec_func in [("TARGET", lambda t,tidx: (t["values"],t["values"])),
                              ("ACHIEVEMENT", lambda t,tidx: (
                                  next((a["values"] for a in achievements if a["area"].lower()==t["area"].lower() and a["branch"].lower()==t["branch"].lower()),[{"c":0,"a":0}]*len(projects)),
                                  None
                              )),
                              ("VARIANCE", lambda t,tidx: (
                                  t["values"],
                                  [ {"c": t["values"][i]["c"] - (next((a["values"] for a in achievements if a["area"].lower()==t["area"].lower() and a["branch"].lower()==t["branch"].lower()),[{"c":0,"a":0}]*len(projects)))[i]["c"],
                                     "a": t["values"][i]["a"] - (next((a["values"] for a in achievements if a["area"].lower()==t["area"].lower() and a["branch"].lower()==t["branch"].lower()),[{"c":0,"a":0}]*len(projects)))[i]["a"]} for i in range(len(projects)) ]
                              ))
                             ]:
        aoa.append([sec_name])
        aoa.append(header1)
        for t in targets:
            vals, _ = sec_func(t,0)
            row=[t["area"],t["branch"]]
            tc_total=0
            ta_total=0
            for v in vals:
                c=v["c"]
                a=v["a"]
                tc_total+=c
                ta_total+=a
                row+=[c,a]
            row+=[f"{tc_total}|{ta_total}"]
            aoa.append(row)
        aoa.append([])

    output=BytesIO()
    import xlsxwriter
    wb=xlsxwriter.Workbook(output)
    ws=wb.add_worksheet("MIS")
    for r,row in enumerate(aoa):
        for c,val in enumerate(row):
            ws.write(r,c,val)
    wb.close()
    output.seek(0)
    return output

if st.sidebar.button("⬇ Download Excel"):
    excel_file = to_excel()
    st.sidebar.download_button("Download MIS Excel", data=excel_file,
                                file_name="Target_vs_Achievement.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")




