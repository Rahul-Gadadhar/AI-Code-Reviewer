import streamlit as st
import google.generativeai as genai

# Set up Google Gemini API key
GEMINI_API_KEY = "API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)

def review_code(user_code):
    prompt = f"""
    You are a highly skilled AI code reviewer. Review the following code, correct any errors, and provide an explanation:
    
    Code:
    ```python
    {user_code}
    ```
    
    Output the corrected code and an explanation of the mistakes.
    """
    
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("✨ Smart AI Code Reviewer ✨")
user_code = st.text_area("Paste your Python code here:", height=200)

if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Reviewing your code..."):
            response = review_code(user_code)
        st.subheader("Corrected Code and Explanation:")
        st.markdown(response)
    else:
        st.warning("Please enter some code before submitting.")
