import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_cleaning import clean_data
from src.kpi import calculate_kpis
from src.visualization import create_charts
from src.report import generate_report

st.set_page_config(page_title="Excel Automation PRO", layout="wide")

st.title("📊 Excel Automation PRO Tool")

st.write("Upload your Excel/CSV file to generate automated reports")

# File upload
uploaded_file = st.file_uploader("Upload File", type=["csv", "xlsx"])

if uploaded_file:

    # Save uploaded file temporarily
    temp_path = os.path.join("data", uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Process data
    df = clean_data(temp_path)

    kpis = calculate_kpis(df)

    create_charts(df)

    generate_report(df, kpis)

    # Display Data
    st.subheader("📄 Cleaned Data")
    st.dataframe(df)

    # Display KPIs
    st.subheader("📈 KPIs")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", kpis["Total Revenue"])
    col2.metric("Total Orders", kpis["Total Orders"])
    col3.metric("Avg Order Value", kpis["Avg Order Value"])

    st.write(f"🏆 Top Product: {kpis['Top Product']}")
    st.write(f"📦 Top Category: {kpis['Top Category']}")

    # Show charts
    st.subheader("📊 Charts")

    st.image("output/category.png")
    st.image("output/time.png")

    # Download button
    st.subheader("⬇️ Download Report")

    with open("output/report.xlsx", "rb") as file:
        st.download_button(
            label="Download Excel Report",
            data=file,
            file_name="report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    st.success("✅ Report Generated Successfully!")