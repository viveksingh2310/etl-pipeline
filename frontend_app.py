import streamlit as st
import pandas as pd
import subprocess

st.set_page_config(layout="wide")
st.title("📈 10-Day NSE Stock Data Dashboard (Infosys Example)")

# Step 1: Run ETL pipeline
if st.button("🔁 Run ETL Pipeline"):
    with st.spinner("Running ETL..."):
        result = subprocess.run(["python", "etl_pipeline.py"], capture_output=True, text=True)
        st.success("ETL Complete!")
        st.code(result.stdout)

# Step 2: Load transformed data
try:
    df = pd.read_csv("output/processed.csv")

    # Step 3: Interactive visualization
    st.subheader("📊 Closing Price & Moving Average")
    st.line_chart(df.set_index("date")[["close", "ma_3day"]])

    st.subheader("📉 Volume Traded")
    st.bar_chart(df.set_index("date")["volume"])

    # Data Table
    with st.expander("🔍 View Raw Data"):
        st.dataframe(df)
except Exception as e:
    st.warning("Please run the ETL first to view data.")
