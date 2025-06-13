

import streamlit as st
import hmac

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

####################################################################

from google import genai

client = genai.Client(api_key= st.secrets["api_key"]["api_key"]) #API KEY

st.header("Recommend Yoga/Exercise")

t1 = st.text_input("Gender?")
t2 = st.text_input("Age?")
t3 = st.text_input("Height(cm)?")
t4 = st.text_input("Weight(kg)?")
t5 = st.text_input("Occupation?")
t6 = st.text_input("Available free time?")

def recommend_yoga(t1,t2,t3,t4,t5,t6):

    """
    A placeholder function for exercise plan recommender.
    """
    if not t1.strip():
        return "Please enter text."
    if not t2.strip():
        return "Please enter text."
    if not t3.strip():
        return "Please enter text."
    if not t4.strip():
        return "Please enter text."
    if not t5.strip():
        return "Please enter text."
    if not t6.strip():
        return "Please enter text."
    
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[f"""Generate a suitable exercise plan with Yoga for a user based on the given inputs such Gender: {t1}, Age: {t2}
              Height(cm): {t3}, Weight(kg): {t4}, Occupation: {t5}, Available free-time: {t6}."""]
)

    # This is where your actual logic would go.
    checked_text = f"{response.text}"
    return checked_text


if st.button("Check"):
    if t1 and t2 and t3 and t4 and t5 and t6:
        result = recommend_yoga(t1,t2,t3,t4,t5,t6)
        st.subheader("Result:")
        st.markdown(result)
    else:
        st.warning("Please enter some text.")

# st.markdown("---")
# st.caption("yoga recommendation")