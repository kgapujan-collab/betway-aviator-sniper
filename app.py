import streamlit as st

st.set_page_config(page_title="BETWAY AVIATOR SNIPER V1", page_icon="✈️", layout="centered")

st.markdown("<h1 style='text-align:center;color:gold;'>BETWAY AVIATOR SNIPER V1</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>NEW VISION - AUTO CASHOUT SIGNAL</h3>", unsafe_allow_html=True)

st.warning("Aviator is random! This tool is for risk management only.")

crashes_input = st.text_input("Enter last 10 crashes from Betway (e.g. 1.2, 2.5, 1.01, 5.32)", "1.2, 2.5, 1.01, 5.32, 1.45, 2.1, 1.88, 3.4, 1.05, 2.7")

if st.button("GET SIGNAL ✈️"):
    try:
        crashes = [float(x.strip()) for x in crashes_input.split(",")]
        avg = sum(crashes)/len(crashes)
        if avg < 1.8:
            st.error(f"🔴 WAIT - Avg {avg:.2f}x too low!")
        else:
            st.success(f"🟢 CASHOUT at 1.50x - Safe! Avg {avg:.2f}x")
            st.metric("RECOMMENDED", "1.50x", f"Avg {avg:.2f}x")
            st.balloons()
    except:
        st.error("Use format: 1.2, 2.1, 1.05")

st.markdown("---")
st.markdown("**SPECIAL TODAY ONLY R2500 | DM to get full access**")
