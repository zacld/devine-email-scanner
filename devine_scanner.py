import streamlit as st

def analyze_email(subject, sender, body, headers):
    threat_score = 0
    reasons = []

    suspicious_keywords = ["urgent", "verify", "update", "click here", "suspended", "prize"]
    if any(word in subject.lower() for word in suspicious_keywords):
        threat_score += 2
        reasons.append("Suspicious keyword in subject")

    if any(word in body.lower() for word in suspicious_keywords):
        threat_score += 2
        reasons.append("Suspicious keyword in body")

    if "@" in sender and "reply-to" in headers:
        sender_domain = sender.split("@")[-1]
        reply_domain = headers["reply-to"].split("@")[-1]
        if sender_domain != reply_domain:
            threat_score += 3
            reasons.append("Sender and Reply-To domain mismatch")

    if "attachments" in headers:
        dangerous_types = [".zip", ".exe", ".scr"]
        for attachment in headers["attachments"]:
            if any(attachment.endswith(ext) for ext in dangerous_types):
                threat_score += 4
                reasons.append(f"Dangerous attachment detected: {attachment}")

    if threat_score >= 7:
        threat_level = "high"
    elif threat_score >= 4:
        threat_level = "medium"
    else:
        threat_level = "low"

    return {"threat_level": threat_level, "reason": reasons}

# Streamlit UI
st.title("Devine Email Threat Scanner")

subject = st.text_input("Email Subject", "URGENT: Your account has been suspended")
sender = st.text_input("Sender Email", "support@paypal.com")
body = st.text_area("Email Body", "Click here to verify your account immediately or it will be closed.")
reply_to = st.text_input("Reply-To Header", "support@secure-paypal.com")
attachments = st.text_input("Attachments (comma separated)", "invoice.zip")

if st.button("Analyze Email"):
    headers = {
        "reply-to": reply_to,
        "attachments": [a.strip() for a in attachments.split(",")]
    }
    result = analyze_email(subject, sender, body, headers)
    st.subheader(f"Threat Level: {result['threat_level'].upper()}")
    st.write("Reasons:")
    for reason in result["reason"]:
        st.markdown(f"- {reason}")
