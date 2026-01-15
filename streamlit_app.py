import streamlit as st
import google.generativeai as genai

# إعداد الساروت
genai.configure(api_key="AIzaSyBIAt3tQkwqc4E_ySplkqXbSINeGInRHBs")

# هنا كان المشكل! دابا درنا السمية اللي بانت لينا في التيست
model = genai.GenerativeModel('gemini-2.5-flash')

st.set_page_config(page_title="Amssuɣl Aclḥi", page_icon="ⴰ")
st.title("Amssuɣl Aclḥi")
st.subheader("ⴰⵎⵙⵙⵓⵖⵍ ⵏ ⵜⵛⵍⵃⵉⵜ")

text = st.text_area("Write in English / ⴰⵔⴰ ⵙ ⵜⵏⴳⵍⵉⵣⵜ:", placeholder="Hello world...")

if st.button("Translate / ⵙⵙⵓⵖⵍ"):
    if text:
        with st.spinner('Translating...'):
            try:
                prompt = (
                    f"Translate the following English text to Standard Tachelhit. "
                    f"Use the formal tone and vocabulary found in Tachelhit Wikipedia. "
                    f"Output only the Tifinagh script translation: {text}"
                )
                response = model.generate_content(prompt)
                st.success("Result / ⵜⴰⵢⴰⴼⵓⵜ:")
                st.markdown(f"### {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please write something first.")
