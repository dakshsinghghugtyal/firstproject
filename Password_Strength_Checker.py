import streamlit as st
import string

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐"
)

st.title("🔐 Password Strength Checker")
st.write("Check the strength of your password.")

st.info("Use sample passwords only. Never enter your real password.")

password = st.text_input(
    "Enter a sample password",
    type="password",
    placeholder="Enter password here"
)

if password:
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Contains uppercase letter": any(c.isupper() for c in password),
        "Contains lowercase letter": any(c.islower() for c in password),
        "Contains a number": any(c.isdigit() for c in password),
        "Contains a special character": any(
            c in string.punctuation for c in password
        )
    }

    score = sum(checks.values())

    if score <= 2:
        strength = "Weak"
        st.error("Password Strength: Weak")
    elif score <= 4:
        strength = "Moderate"
        st.warning("Password Strength: Moderate")
    else:
        strength = "Strong"
        st.success("Password Strength: Strong")

    st.subheader("Password Strength Score")
    st.write(f"Score: {score}/5")
    st.progress(score / 5)

    st.subheader("Criteria Checklist")

    for criterion, passed in checks.items():
        if passed:
            st.write(f"✅ {criterion}")
        else:
            st.write(f"❌ {criterion}")

    st.subheader("Suggestions")

    suggestions = []

    if not checks["At least 8 characters"]:
        suggestions.append("Use at least 8 characters.")

    if not checks["Contains uppercase letter"]:
        suggestions.append("Add an uppercase letter (A-Z).")

    if not checks["Contains lowercase letter"]:
        suggestions.append("Add a lowercase letter (a-z).")

    if not checks["Contains a number"]:
        suggestions.append("Include at least one number.")

    if not checks["Contains a special character"]:
        suggestions.append("Add a special character, such as @, #, or !.")

    if suggestions:
        for suggestion in suggestions:
            st.write(f"• {suggestion}")
    else:
        st.write("Great! All five criteria are satisfied.")

    st.caption(
        "This is a basic educational checker. "
        "A strong score does not guarantee complete security."
    )

else:
    st.write("Enter a sample password to begin the analysis.")
