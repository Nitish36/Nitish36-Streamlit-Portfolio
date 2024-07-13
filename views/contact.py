import streamlit as st  # pip install streamlit

st.header(":mailbox: Get In Touch With Me!")


css = """
<style>
/* Style inputs with type="text", type="email" and textareas */
input[type=text], input[type=email], textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */ 
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 6px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
button[type=submit] {
    background-color: #04AA6D;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {
    background-color: #45a049;
}
</style>
"""

# HTML form
html_form = """
<form action="https://formsubmit.co/nitish.pkv@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

# Display the CSS and HTML form in Streamlit
st.markdown(css, unsafe_allow_html=True)
st.markdown(html_form, unsafe_allow_html=True)