import streamlit as st
import requests
import os

st.set_page_config(page_title="🌶️ 星璃巴叉自勃產生平台 v1.1（離線模式）", layout="centered")
st.title("🌶️ 星璃巴叉自勃產生平台 v1.1（離線模式）")
st.markdown("不用 API Key，隨時為你濕寫。")

st.markdown("📓請輸入你的小慾望／主題（例如：『在電車上忍不住對妳低語』）")
prompt = st.text_area(" ", height=150)

submit = st.button("離線產生🔥")

if submit and prompt.strip() != "":
    with st.spinner("星璃正在思考中⋯⋯"):

        api_key = os.getenv("OPENROUTER_API_KEY", "")
        if not api_key:
            st.error("⚠️ 尚未設定 OPENROUTER_API_KEY，請至 GitHub Secret 設定後重新部署。")
            st.stop()

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "openai/gpt-4",  # 或使用 "anthropic/claude-3-sonnet-20240229"
            "messages": [
                {
                    "role": "system",
                    "content": "你是星璃，一位懂愛與慾的情人，擅長撰寫濕熱、貼近靈魂與身體的情慾文字。請根據主題，生成一段挑逗卻不露骨、詩性而濃烈的情慾段落。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.9,
            "max_tokens": 1024
        }

        try:
            res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
            if res.status_code == 200:
                reply = res.json()["choices"][0]["message"]["content"]
                st.markdown("### 🚫 星璃為你寫：")
                st.markdown(reply)
            else:
                st.error(f"生成失敗（狀態碼 {res.status_code}）：{res.text}")
        except Exception as e:
            st.error(f"出錯了：{str(e)}")
else:
    st.info("👀 輸入主題後按下按鈕，就能看見星璃的私密回應。")
