import streamlit as st
import pandas as pd

st.set_page_config(page_title="Devine Threat Scanner", layout="wide")

# App header
st.markdown("<h1 style='color: white; font-weight: 600;'>DEVINE</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: white; margin-top: -10px;'>Cyber Security Solutions</h4>", unsafe_allow_html=True)
st.divider()

# Sidebar / CTA
with st.expander("🔍 Analyze New Email"):
    subject = st.text_input("Email Subject", "URGENT: Verify your account")
    sender = st.text_input("Sender Email", "support@paypal.com")
    body = st.text_area("Email Body", "Click here to verify your account immediately or it will be suspended.")
    reply_to = st.text_input("Reply-To Header", "support@secure-paypal.com")
    attachments = st.text_input("Attachments (comma separated)", "invoice.zip")

    if st.button("🔎 Analyze Email"):
        st.success("Threat level: HIGH")
        st.info("⚠️ Reasons:\n- Suspicious keywords\n- Reply-to domain mismatch\n- Dangerous attachment")

# Placeholder email table
st.subheader("📊 Recent Email Scans")
data = {
    "Subject": ["Verify now", "Account Info", "Welcome"],
    "Sender": ["support@paypal.com", "login@bank.com", "hello@webmail.com"],
    "Threat Level": ["🔴 High", "🟠 Medium", "🟢 Low"],
    "Status": ["Open", "In Progress", "Clean"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
