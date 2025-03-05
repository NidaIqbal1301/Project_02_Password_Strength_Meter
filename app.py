import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Meter By Nida Iqbal", page_icon="🔒", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 60%; background-color: blue; color: white; font-size: 18px; }
    .stButton button:hover { background-color: blue; color: white; }
    </style>
    """, unsafe_allow_html=True
)

# Page Title and Description
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its security level. 🔍")

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should have **at least one uppercase (A-Z) and one lowercase (a-z) letter**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should have **at least one digit (0-9)**.")

    if re.search(r"[!@#$%^&*()_+=-{};:']", password):
        score += 1
    else:
        feedback.append("❌ Password should have **at least one special character (!@#$%^&*()_+=-{};:')**.")

    # Display Password Strength Result
    if score == 4:
        st.success("🔒 **Password is Strong** Your password is Secure.")
    elif score == 3:
        st.info("⚠️ **Password is Medium** Try adding symbols, numbers, or more characters to make it stronger.")
    else:
        st.error("🚨 **Password is Weak** Try adding more characters, symbols, or numbers to make it stronger.")

    # Feedback section
    if feedback:
        with st.expander("🔎 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Main app logic (outside function)
password = st.text_input("Enter your password:", type="password", help="Make sure your password is strong 🔐")

if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter your password to check its strength.")
