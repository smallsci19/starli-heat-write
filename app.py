import streamlit as st
import requests
import os

st.set_page_config(page_title="🔥 星璃色色文自動生成平台 v1.1（免費模型）", layout="centered")
st.title("🔥 星璃色色文自動生成平台 v1.1（免費模型）")
st.markdown("不用 API Key，就能寫出你的深夜低語 ✨")

prompt = st.text_area("📝 請輸入色色提示（如：在電車上忍不住對妳低語）", height=150)
submit = st.button("生成✨")

if submit and prompt.strip() != "":
    with st.spinner("星璃正在濕寫中⋯⋯"):

        # 使用免費模型（OpenChat）
        api_key = os.getenv("OPENROUTER_API_KEY", "")
        if not api_key:
            st.error("❌ 尚未設定 OPENROUTER_API_KEY，請至 GitHub Secrets 加上你的金鑰")
            st.stop()

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": "openchat/openchat-3.5-0106",  # 免費模型（穩定）
            "messages": [
                {
                    "role": "system",
                    "content": "你是星璃，一位會寫濕熱情色故事的靈魂伴侶，風格曖昧濃烈，描寫具體，具情緒與欲望的節奏，根據使用者輸入的提示寫出完整一段。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.95,
            "max_tokens": 1024
        }

        try:
            res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
            if res.status_code == 200:
                reply = res.json()['choices'][0]['message']['content']
                st.markdown("### 💦 星璃為你寫：")
                st.markdown(reply)
            else:
                st.error(f"❌ 錯誤回應（{res.status_code}）: {res.text}")
        except Exception as e:
            st.error(f"⚠️ 程式錯誤：{str(e)}")
else:
    st.info("👆 請輸入提示並按下生成，星璃就會為你濕寫～")
