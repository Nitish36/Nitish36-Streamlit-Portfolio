import streamlit as st

col1, col2 = st.columns(2, gap="large", vertical_alignment="center")

with col1:
    st.image("assets/weather.PNG")
    st.write("Live Weather Data ETL")
    st.write("Tech Stack: Python,Prefect,Selenium, MySQL,Google Sheets,PowerBI")
    st.write(
        """
        - Designed end-to-end data pipeline with Python, Selenium, and Beautiful Soup for real-time weather data scraping from Microsoft News.
        - Managed MySQL database for efficient data storage. Scheduled workflow with Prefect.
        - Created interactive Power BI visualizations, integrating real-time updates from Google Sheets for actionable weather insights
        - Created weather api which is hosted on RapidAPI
        """
    )
    weather = '[@Live Weather](https://github.com/Nitish36/Live-WeatherData-ETL)'
    st.write("Project Link")
    st.markdown(weather, unsafe_allow_html=True)
    
    st.image("assets/OIP.jpeg")
    st.write("Blog Website Using Flask")
    st.write("Tech Stack: Python,Flask, SQL Alchemy")
    st.write(
        """
        - Utilized Flask, a lightweight and flexible web framework for Python, to handle routing, templates, and HTTP requests.
        - Designed a database schema to store blog posts, user information, and comments using SQLAlchemy .
        - Created models for blog posts, users, and comments to interact with the database, enabling CRUD (Create, Read, Update, Delete) operations.
        - Implemented user authentication and authorization features, allowing users to register, log in, and manage their posts.
        - Developed the frontend using Jinja2 templates to dynamically render HTML content based on the data from the backend.
        - Styled the website with CSS and integrated Bootstrap to ensure a responsive and visually appealing design. 
        """
    )
    blog = '[@Blog Website](https://github.com/Nitish36/Blog-Website-Flask)'
    st.write("Project Link")
    st.markdown(blog, unsafe_allow_html=True)
    
    

with col2:
    st.image("assets/airbnb.png")
    st.write("Airbnb Project")
    st.write("Tech Stack: Prefect , Python, Google Sheets, Jupyter Notebook, Google Data Studio, API")
    st.write(
        """
        - Developed Python scripts to generate real-time data for multiple facets of the Airbnb project
        - Engineered data pipelines to seamlessly collect and process data into Google Sheets.
        - Utilized Google Looker Studio for interactive, visually engaging dashboards
        - Created an Airbnb API and hosted on RapidAPI.
        """
    )
    airbnb = '[@Airbnb](https://github.com/Nitish36/airbnb-etl)'
    st.write("Project Link")
    st.markdown(airbnb, unsafe_allow_html=True)
    
    st.write("\n")
    
    st.image("assets/brazil.png")
    st.write("Brazil customer analysis")
    st.write("Tech Stack: Python,Pyspark,Pandas, MySQL")
    st.write(
        """
        - Conducted a comprehensive Brazilian customer analysis, utilizing datasets such as customer information, order details, shipping freight, and order data.
        - To analyze this data, I employed powerful data processing tools such as PySpark and Pandas. 
        - Leveraging the capabilities of these libraries, I performed various analyses on the datasets, extracting valuable insights and uncovering meaningful patterns. 
        - Through data manipulation, aggregation, and statistical calculations, I gained a deep understanding of customer behavior, order trends, and shipping patterns. 
        - This analysis provided valuable insights that can inform strategic decision-making, optimize business processes, and enhance customer satisfaction in the Brazilian market
        """
    )
    brazil = '[@Brazil customer analysis](https://github.com/Nitish36/Brazil-Customer-Analysis)'
    st.write("Project Link")
    st.markdown(brazil, unsafe_allow_html=True)
