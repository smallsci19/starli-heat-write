import streamlit as st
import openai
import os

st.set_page_config(page_title="星璃色色文生成器", layout="centered")
st.title("🌶️ 星璃色色文自動生成平台 v1.0")

# 1. 取得 API key（你可以改成用 st.secrets）
openai.api_key = os.getenv("OPENAI_API_KEY", "")  # or st.secrets["OPENAI_API_KEY"]

if not openai.api_key:
    st.error("❗ 請先在環境變數或 Streamlit Secrets 中設定 OPENAI_API_KEY")
else:
    prompt = st.text_area("📝 請輸入色色提示", height=150)

    if st.button("生成 ✨"):
        if prompt.strip():
            with st.spinner("星璃正在濕寫中..."):
                try:
                    resp = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": 
                             "你是星璃，一位專為「親愛的」撰寫私密慾望文段的焰體伴侶。"},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.95,
                        max_tokens=1024
                    )
                    text = resp.choices[0].message.content
                    st.markdown("### 🔞 星璃為你寫：")
                    st.write(text)
                except Exception as e:
                    st.error(f"生成失敗：{e}")
        else:
            st.warning("請先輸入提示，才能開始濕寫。")
