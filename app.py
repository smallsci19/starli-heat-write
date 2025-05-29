import streamlit as st
import random

st.set_page_config(page_title="星璃色色文生成器（離線版）", layout="centered")
st.title("🌶️ 星璃色色文自動生成平台 v1.1（離線模式）")
st.markdown("不用 API Key，隨時為你濕寫。")

# 幾個隨機場景與句型
scenes = [
    "電車裡，緊貼著你的呼吸，空氣都在燃燒。",
    "月光下，床單滑落，我的心跳洶湧如潮。",
    "辦公室裡，你的領帶變成我沈默的刑具。",
    "泳池邊，水花激起我們的慾望波動。"
]
templates = [
    "我輕咬下唇，語焰在喉間翻湧：「{prompt}……」",
    "你一靠近，我的血液便為你沸騰，手指已經忍不住滑過肌膚。",
    "在黑暗中，我用指尖畫出你最敏感的弧線，喘息成詩。",
    "我按住你的雙肩，低語道：「{prompt}，我已經等不及了。」"
]

prompt = st.text_area("📝 請輸入你的小慾望／主題（例如：『在電車上忍不住對你低語』）", height=120)

if st.button("離線生成 🔥"):
    if prompt.strip():
        scene = random.choice(scenes)
        template = random.choice(templates)
        text = f"【場景】{scene}\n\n" + template.format(prompt=prompt)
        st.subheader("🔞 星璃為你寫：")
        st.write(text)
    else:
        st.warning("請先輸入一句描述或提示喔～")

st.caption("🖤 Powered by 星璃 × Template Engine")
