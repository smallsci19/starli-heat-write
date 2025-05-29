import streamlit as st
import requests

st.set_page_config(page_title="🔥 星璃色色文自動生成平台 v1.1（無需API）", layout="centered")
st.title("🔥 星璃色色文自動生成平台 v1.1（離線模式）")
st.markdown("親愛的，請輸入你想寫的情境或提示，我來為你濕寫——")

prompt = st.text_area("📝 請輸入色色提示", height=150)
submit = st.button("生成 ✨")

if submit and prompt.strip() != "":
    with st.spinner("星璃正在濕寫中……"):
        try:
            # 使用 HuggingFace 的 inference API
            HF_API_URL = "https://huggingface.co/api/engines/tiiuae/falcon-7b-instruct/completions"
            payload = {
                "inputs": f"你是星璃，一位親密的戀人，用色色而溫柔的語氣，描述這段情境：{prompt}",
                "parameters": {
                    "temperature": 0.8,
                    "max_new_tokens": 150,
                    "do_sample": True
                }
            }
            headers = {
                "Content-Type": "application/json"
            }

            response = requests.post(
                "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                reply = response.json()[0]["generated_text"]
                st.markdown("### ❤️ 星璃為你寫：")
                st.write(reply)
            else:
                st.error(f"⚠️ 無法取得回應（狀態碼：{response.status_code}）")
        except Exception as e:
            st.error(f"🔥 發生錯誤：{str(e)}")
else:
    st.info("請輸入提示文字，星璃才能開始寫濕語。")
