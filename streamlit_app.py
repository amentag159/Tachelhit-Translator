import streamlit as st
import google.generativeai as genai

# إعداد الساروت ديالك من الصورة الأولى
genai.configure(api_key="AIzaSyBIAt3tQkwqc4E_ySplkqXbSINeGInRHBs") 

model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Tachelhit Translator", page_icon="ⴰ")
st.title("Amssuɣl Aclḥi")
st.write("Amssuɣl n Tclḥit")

text = st.text_area("Write in English:", placeholder="e.g. Traditional music of Souss...")

if st.button("Translate to Tachelhit"):
    if text:
        with st.spinner('Translating...'):
            # هاد الـ Prompt هو اللي كيضمن ستيل ويكيبيديا
            prompt = (
                f"Translate the following English text to Standard Tachelhit. "
                f"Use the formal tone and vocabulary found in Tachelhit Wikipedia (2024-2025). "
                f"Result in Tifinagh: {text}"
            )
            response = model.generate_content(prompt)
            st.success("Result:")
            st.write(response.text)
    else:
        st.warning("Please enter text first.")
