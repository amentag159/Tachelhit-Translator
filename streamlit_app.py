import streamlit as st
import google.generativeai as genai

# 1. حطي هنا ساروت "Shilha" اللي كيسالي بـ EsO0
genai.configure(api_key="AIzaSyDXAWkCHFY8-7hTOygelQPtB2oIHi3EsO0") 

# 2. إعداد الموديل بأسلوب Wikipedia Tachelhit والاسم الجديد
system_instruction = (
    "You are 'Shi trans', an expert translator for Standard Tachelhit. "
    "Your style must match Wikipedia Tachelhit (Shiwiki). "
    "Use formal vocabulary, correct grammar, and write in Latin script. "
    "Avoid creative paraphrasing; stay loyal to the encyclopedic tone of Wikipedia."
)

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_instruction
)

# إعداد واجهة الموقع بالاسم الجديد
st.set_page_config(page_title="Shi trans", page_icon="ⴰ")
st.title("Shi trans | ⵛⵉ ⵜⵔⴰⵏⵙ")
st.markdown("##### ⴰⵎⵙⵙⵓⵖⵍ ⵏ ⵜⵛⵍⵃⵉⵜ (Wikipedia Style)")

# خانة الكتابة
text = st.text_area("Write in English / ⴰⵔⴰ ⵙ ⵜⵏⴳⵍⵉⵣⵜ:", placeholder="Type here...")

if st.button("Translate / ⵙⵙⵓⵖⵍ"):
    if text:
        with st.spinner('Processing...'):
            try:
                # طلب الترجمة بأسلوب ويكيبيديا
                response = model.generate_content(text)
                st.success("Result / ⵜⴰⵢⴰⴼⵓⵜ:")
                st.markdown(f"### {response.text}")
            except Exception as e:
                if "429" in str(e):
                    st.error("Quota exceeded: جربي مرة أخرى بعد دقيقة.")
                else:
                    st.error(f"Error: {e}")
    else:
        st.warning("Please enter text.")
