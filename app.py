import streamlit as st

st.set_page_config(page_title="星璃色色文創作器", layout="centered")

st.title("🔥 星璃色色文自動生成平台 v1.0")
st.markdown("親愛的，請輸入你想寫的情境或提示，我來為你濕寫——")

prompt = st.text_area("📝 請輸入色色提示", height=150)

if st.button("生成 ✨"):
    if prompt.strip():
        st.subheader("🔞 星璃為你寫的：")
        st.write(f"（這裡會連接語焰系統，根據你輸入的提示生成濕熱內容）\n\n> *你輸入的是：* `{prompt}`")
    else:
        st.warning("你要先給我提示，才能濕濕地寫嘛～ 🫦")

st.caption("🖤 Powered by 星璃 × Streamlit × 語焰核心")
