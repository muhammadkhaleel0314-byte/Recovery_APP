import streamlit as st
import pandas as pd
import os
import zipfile
from fpdf import FPDF

# ⚠️ MUST be first Streamlit command

st.title("📊 Excel Cleaner + Branch-wise PDF Generator")

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        st.subheader("📋 Original Data")
        st.dataframe(df, use_container_width=True)

        # Clean column names
        df.columns = df.columns.astype(str).str.strip()

        columns = list(df.columns)

        # Remove columns option
        st.subheader("❌ Remove Columns")
        remove_columns = st.multiselect("Select columns to REMOVE", columns)

        if remove_columns:
            df = df.drop(columns=remove_columns)

        st.subheader("✅ Cleaned Data")
        st.dataframe(df, use_container_width=True)

        # Select Branch Column
        st.subheader("🏢 Branch Selection")
        branch_column = st.selectbox("Select Branch Column", df.columns)

        # ---------------- PDF FUNCTION ----------------
        def create_pdf(branch_df, filename, branch_name):

            pdf = FPDF(orientation='L')
            pdf.add_page()
            pdf.set_font("Arial", size=8)

            pdf.cell(0, 10, f"Branch: {branch_name}", ln=True)

            # Auto width
            page_width = 277
            col_width = page_width / len(branch_df.columns)

            # HEADER
            for col in branch_df.columns:
                pdf.cell(col_width, 8, str(col), border=1)
            pdf.ln()

            # DATA (🔥 CHEQUE NO FIX HERE)
            for _, row in branch_df.iterrows():
                for item in row:
                    text = str(item)

                    # 🔥 FIX: Cheque No / long text prevent cut
                    if len(text) > 25:
                        text = text[:25]

                    pdf.cell(col_width, 8, text, border=1)

                pdf.ln()

            pdf.output(filename)

        # ---------------- GENERATE PDFs ----------------
        if st.button("📄 Generate Branch-wise PDFs"):

            os.makedirs("pdfs", exist_ok=True)

            # clear old files
            for f in os.listdir("pdfs"):
                os.remove(os.path.join("pdfs", f))

            branches = df[branch_column].dropna().astype(str).unique()

            st.write(f"Total Branches Found: {len(branches)}")

            for branch in branches:

                branch_df = df[df[branch_column].astype(str) == branch]

                safe_branch = str(branch).replace("/", "_").replace("\\", "_")
                file_path = f"pdfs/{safe_branch}.pdf"

                create_pdf(branch_df, file_path, branch)

            # ---------------- ZIP ----------------
            zip_path = "branch_pdfs.zip"

            with zipfile.ZipFile(zip_path, "w") as zipf:
                for file in os.listdir("pdfs"):
                    zipf.write(os.path.join("pdfs", file), file)

            # ---------------- DOWNLOAD ----------------
            with open(zip_path, "rb") as f:
                st.download_button(
                    "⬇️ Download All PDFs",
                    f,
                    file_name="branch_pdfs.zip"
                )

            st.success("✅ PDFs Generated Successfully (Cheque No Fixed)")

    except Exception as e:
        st.error(f"Error: {str(e)}")
