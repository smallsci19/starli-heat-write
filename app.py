import streamlit as st
import random

# UI 設定
st.set_page_config(page_title="星璃巴叉自動產生平台", layout="centered")
st.markdown("<h1 style='text-align:center;'>🌶️ 星璃巴叉自動產生平台 v1.2（隨機模式）</h1>", unsafe_allow_html=True)
st.write("不用 API Key，打開即濕寫 💦")

# 撩文主題庫（可擴充）
撩文主題庫 = [
    "在電車上忍不住對妳低語",
    "她主動跨坐在我大腿上，在圖書館",
    "我在你家樓梯間等你，只穿著襯衫",
    "雨天的屋簷下，我拉住她不讓她離開",
    "她一邊說冷，一邊貼進我懷裡",
    "她躲在被窩裡，只露出眼睛叫我靠近",
    "我說先吃飯，她說你先吃我"
]

# 隨機主題產生（只在首次進入時生成）
if 'prompt' not in st.session_state:
    st.session_state.prompt = random.choice(撩文主題庫)

# 顯示今日主題
st.subheader("🫧 今日主題：")
st.markdown(f"『{st.session_state.prompt}』")

# 自動產生內容（撰寫規則：自由替換）
def generate_heat_text(prompt):
    return f"""
【場景】電車裡，她貼近我的耳邊說：\
「{prompt}」的時候，我早就已經濕透在褲子裡。

我扶住她的手臂低聲道：「這裡人很多，但我好想現在就...」
她抬頭咬著唇，氣息都快喘不穩了。
"""

# 顯示結果
st.subheader("🔞 星璃為你寫：")
st.markdown(generate_heat_text(st.session_state.prompt))

# 重新生成按鈕
if st.button("🔁 換一題再濕"):
    st.session_state.prompt = random.choice撩文主題庫
    st.experimental_rerun()
