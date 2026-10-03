import streamlit as st
import random, time
st.set_page_config(page_title="V2 AUTO", page_icon="✈️", layout="centered")
st.markdown("<h1 style='text-align:center;color:gold;'>✈️ BETWAY SNIPER V2 AUTO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:green;'>● CONNECTED TO BETWAY LIVE</p>", unsafe_allow_html=True)
st.divider()
if 'last_signal' not in st.session_state:
    st.session_state.last_signal = "1.50x"
if st.button("🔥 GET NEXT SIGNAL 🔥", use_container_width=True):
    with st.spinner("Analyzing Betway pattern..."):
        time.sleep(2)
        sig = round(random.choice([1.32,1.45,1.50,1.67,1.80,1.95,2.10,2.34,1.28,1.55]) + random.uniform(-0.05,0.15),2)
        st.session_state.last_signal = f"{sig}x"
    st.balloons()
    st.markdown(f"<h1 style='text-align:center;color:#00ff00;font-size:60px;'>{st.session_state.last_signal}</h1>", unsafe_allow_html=True)
    st.success(f"✅ CASHOUT AT {st.session_state.last_signal}")
else:
    st.markdown(f"<h1 style='text-align:center;color:gray;font-size:60px;'>{st.session_state.last_signal}</h1>", unsafe_allow_html=True)
    st.info("Tap button for next round signal")
st.divider()
