import streamlit as st
import google.generativeai as genai

# الساروت ديالك
genai.configure(api_key="AIzaSyBIAt3tQkwqc4E_ySplkqXbSINeGInRHBs")

st.title("🔍 كشف الموديلات (Test)")

if st.button("Check Available Models"):
    try:
        st.write("جاري البحث عن الموديلات المتوفرة...")
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        if available_models:
            st.success("الموديلات اللي عندك الحق تخدمي بيها:")
            for model in available_models:
                st.code(model) # غادي يكتب لينا السمية الصحيحة
        else:
            st.error("اللائحة خاوية! الساروت خدام ولكن ما عندك تا موديل مفعل.")
            
    except Exception as e:
        st.error(f"مشكل في الساروت أو الاتصال: {e}")
