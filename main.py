import streamlit as st
from PIL import Image


about_page = st.Page(
    page="views/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

experience_page = st.Page(
    page="views/experience.py",
    title="Experience",
    icon=":material/corporate_fare:",
)

project_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon=":material/bar_chart:",
)

contact = st.Page(
    page="views/contact.py",
    title="Contact",
    icon=":material/account_circle:",
)

pg = st.navigation(pages=[about_page, experience_page, project_page, contact])

st.markdown("""
<style>
img[data-testid="stLogo"] {
    height: 10.5rem;
}

@media (max-width: 767px) {
    img[data-testid="stLogo"] {
        height: 4rem;  /* Adjust the height for smaller screens */
    }
}
</style>
""", unsafe_allow_html=True)


# Display the logo
st.logo("assets/leo.png")
st.sidebar.text("Made with ❤️ by Nitish")
st.sidebar.text('Phone: +91 7975722193')
st.sidebar.text('Email: nitish.pkv@gmail.com')
pg.run()
