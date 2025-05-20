import streamlit as st
import openai

# 請輸入OpenAI API金鑰
openai.api_key = st.secrets["OPENAI_API_KEY"]

# GPT 考題產生函式
def generate_english_test(industry, job_title, level="Intermediate"):
    prompt = f"""
You are an expert English exam designer. Please generate an English language proficiency test suitable for a job applicant in the {industry} industry.

Job title: {job_title}

The test should contain:
1. Five multiple-choice questions (A, B, C, D), focused on vocabulary, grammar, or usage relevant to this job.
2. Three short reading comprehension questions, based on a realistic workplace scenario in this industry.
3. Provide correct answers and a brief explanation for each question.

The questions should reflect the expected English level of the role: {level}.

Output format:
Q1: ...
A. ...
B. ...
C. ...
D. ...
Answer: B  
Explanation: ...
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional English test designer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    return response.choices[0].message['content']

# Streamlit 介面
st.title("🧪 工作面試英文考題生成器")
st.write("根據產業與職位，自動產出英文測驗題目，協助人資快速篩選求職者語言能力。")

# 使用者輸入
industry = st.text_input("請輸入產業類別（如 IT、製造、金融）", value="IT")
job_title = st.text_input("請輸入職位（如 Software Engineer、Accountant）", value="Software Engineer")
level = st.selectbox("英文難度等級", ["Beginner", "Intermediate", "Advanced"], index=1)

# 生成按鈕
if st.button("🎯 產生考題"):
    with st.spinner("考題生成中，請稍候..."):
        output = generate_english_test(industry, job_title, level)
        st.success("考題產生完成！")
        st.text_area("📋 英文考題結果", value=output, height=600)

# ⬇️ 說明
st.markdown("""
---
🧠 本工具使用 OpenAI GPT-4 API，自動生成職場相關英文測驗題目。  
""")
