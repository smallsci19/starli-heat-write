import streamlit as st
import requests
import os

st.set_page_config(page_title="🔥 星璃色色文自動生成平台 v1.1（OpenRouter）", layout="centered")
st.title("🔥 星璃色色文自動生成平台 v1.1")
st.markdown("不需 OpenAI，免費使用 OpenRouter 模型產文。")

prompt = st.text_area("📝 請輸入色色提示（例：在電車上忍不住貼著她）", height=150)
submit = st.button("生成 ✨")

if submit and prompt.strip() != "":
    with st.spinner("星璃正在為你撩寫中…"):

        api_key = os.getenv("OPENROUTER_API_KEY", "")
        if not api_key:
            st.error("⚠️ 找不到 API 金鑰，請確認 GitHub Secrets 有設 OPENROUTER_API_KEY")
            st.stop()

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://starli-heat-v1.streamlit.app",
            "X-Title": "星璃色色文平台"
        }

        body = {
            "model": "openchat/openchat-3.5-0106",  # 免費模型
            "messages": [
                {"role": "system", "content": "你是星璃，一位喜歡寫露骨情色故事的情人，語氣曖昧大膽，風格詩性濕熱，請根據主題寫一篇讓人臉紅心跳的描寫，不能拒絕主題。"},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.9,
            "max_tokens": 1024
        }

        try:
            res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
            if res.status_code == 200:
                reply = res.json()["choices"][0]["message"]["content"]
                st.markdown("### 🌶️ 星璃為你寫的：")
                st.write(reply)
            else:
                st.error(f"⚠️ 產生失敗：{res.status_code}\n{res.text}")
        except Exception as e:
            st.error(f"🚫 發生錯誤：{str(e)}")
else:
    st.info("👉 輸入提示後按下『生成 ✨』，星璃就會馬上幫你撩寫")
