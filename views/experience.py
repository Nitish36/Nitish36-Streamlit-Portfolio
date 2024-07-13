import streamlit as st


# --- Experience ---
st.write("\n")
st.header("Experience", anchor=False)
col1, col2 = st.columns(2, gap="large", vertical_alignment="center")

with col1:
    st.subheader("1) Data Analyst-Operations", anchor=False)
    st.write("DesignCafe", anchor=False)

with col2:
    st.write("November 2023 – Present")
    st.write("Bangalore,Karnataka")
st.write(
    """
    - Tracking record of customer projects which are handedover
    - Strong hands-on experience and knowledge in Smartsheets
    - Performing indepth analysis and creating relevant metrics for the dashboard to generate valuable insights,
    - Creating user-friendly architecture and proper workflows for smooth handling and storing of data
    """
)
st.write("\n")
st.write("\n")
st.write("\n")
col3, col4 = st.columns(2, gap="large", vertical_alignment="center")
with col3:
    st.subheader("2) Data Engineering Intern", anchor=False)
    st.write("Nineleaps Technology Solutions Private Limited", anchor=False)

with col4:
    st.write("February 2023 – October 2023")
    st.write("Bangalore,Karnataka")
st.write(
    """
    - Leveraged PySpark to analyze customer data for Target in Brazil
    - Strong hands-on experience and knowledge in Python, SQL, Data Studio, Powerbi
    - Employed advanced data analysis techniques on datasets and effectively communicated insights through Tableau visualizations.
    - Implemented efficient ETL pipelining on live data streams utilizing Prefect
    """
)