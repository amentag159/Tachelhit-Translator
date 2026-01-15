import streamlit as st
import google.generativeai as genai

# درنا الكود ديالك نيت، ولكن بدلنا الموديل لتحت
genai.configure(api_key="AIzaSyBIAt3tQkwqc4E_ySplkqXbSINeGInRHBs") 

# التغيير المهم: بدلنا flash بـ pro باش يخدم ليك دابا
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Amssuɣl Aclḥi", page_icon="ⴰ")
st.title("Amssuɣl Aclḥi - ⴰⵎⵙⵙⵓⵖⵍ ⴰⵛⵍⵃⵉ")
st.write("مترجم الإنجليزية لتاشلحيت (أسلوب ويكيبيديا)")

text = st.text_area("Write in English:", placeholder="e.g. Traditional music of Souss...")

if st.button("Translate to Tachelhit"):
    if text:
        with st.spinner('Translating...'):
            try:
                # الستيل ديال الترجمة
                prompt = (
                    f"Translate the following English text to Standard Tachelhit. "
                    f"Use the formal tone and vocabulary found in Tachelhit Wikipedia (2024-2025). "
                    f"Result in Tifinagh script: {text}"
                )
                response = model.generate_content(prompt)
                st.success("Result / ⵜⴰⵢⴰⴼⵓⵜ:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter text first.")
