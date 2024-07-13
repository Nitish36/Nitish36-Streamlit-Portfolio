import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/img2.jpeg", width=230)

with col2:
    st.title("Nitish K", anchor=False)
    st.write('An aspiring Data analyst well versed in SQL, Python, Excel and Data Studio')
    col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
    with col3:
        github = '[@GitHub](http://github.com/Nitish36)'
        linkedin = '[@Linkedin](https://www.linkedin.com/in/nitish-k-5431641b2)'
        kaggle = '[@Kaggle](https://www.kaggle.com/bishop36)'
        st.markdown(github, unsafe_allow_html=True)
        st.markdown(linkedin, unsafe_allow_html=True)
        st.markdown(kaggle, unsafe_allow_html=True)
    with col4:
        apis = '[@RapidAPI](https://rapidapi.com/user/nitishpkv)'
        whatsapp = '[@Whatsapp](https://wa.me/+917975722193)'
        w3 = '[@W3Schools](https://www.w3profile.com/nitish36)'
        st.markdown(apis, unsafe_allow_html=True)
        st.markdown(whatsapp, unsafe_allow_html=True)
        st.markdown(w3, unsafe_allow_html=True)

# --- QUALIFICATIONS ---
st.write("\n")
st.subheader("Qualifications", anchor=False)
st.write(
    """
    - Passionate fresh graduate with a solid 11-month track record in data analytics.
    - Strong hands-on experience and knowledge in Python, SQL and Excel
    - Ready to transform raw data into actionable insights,
    - I thrive on unraveling complex patterns and turning them into compelling stories for informed decision-making.
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - Languages: Python, SQL, Java, HTML,CSS, Git
    - Databases: MYSQL Workbench, Microsoft SQL Server, Excel, Google Sheets
    - Visualization Tools: Tableau, PowerBI, Google Data Studio
    - ETL Tools: Prefect, SSIS
    - Developer Tools: VS Code, PyCharm, Sublime Text Editor
    - Libraries: Scrapy, BeautifulSoup, Pandas, Numpy, Matplotlib,Seaborn
    - Automation Tool: Selenium
    """
)

# --- Education ---
st.write("\n")
st.subheader("Education", anchor=False)
col5, col6 = st.columns(2, gap="large", vertical_alignment="center")
with col5:
    st.subheader("Bachelor of Engineering in Computer Science", anchor=False)
    st.write("RNS INSTITUTE OF TECHNOLOGY", anchor=False)

with col6:
    st.write("Aug. 2019 – May 2023")
    st.write("Bangalore,Karnataka")