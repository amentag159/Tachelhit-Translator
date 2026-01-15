import streamlit as st
import google.generativeai as genai

# إعداد الساروت ديالك
genai.configure(api_key="AIzaSyBIAt3tQkwqc4E_ySplkqXbSINeGInRHBs") 

# بدلنا الموديل هنا باش يخدم ليك
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Amssuɣl Aclḥi", page_icon="ⴰ")
st.title("Amssuɣl Aclḥi")
st.write("Amssuɣl n Tclḥit")

text = st.text_area("Write in English:", placeholder="e.g. Traditional music of Souss...")

if st.button("Translate to Tachelhit"):
    if text:
        with st.spinner('Translating...'):
            try:
                # هاد الـ Prompt هو اللي كيضمن ستيل ويكيبيديا
                prompt = (
                    f"Translate the following English text to Standard Tachelhit. "
                    f"Use the formal tone and vocabulary found in Tachelhit Wikipedia (2024-2025). "
                    f"Result in Tifinagh: {text}"
                )
                response = model.generate_content(prompt)
                st.success("Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter text first.")
