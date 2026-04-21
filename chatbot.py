import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="NSTI Dashboard", layout="wide")

import base64

# ---------- BACKGROUND IMAGE FUNCTION ----------
def add_bg_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(255, 255, 255, 0.85),
                rgba(255, 255, 255, 0.85)
            ),
            url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# CALL FUNCTION
add_bg_image("nsti.jpg")

# ---------- SIDEBAR ----------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "🎓 Eligibility & Checker",
    "📄 Documents",
    "🤖 AI Assistant"
])

# ---------- HOME ----------
if page == "🏠 Home":

    st.title("🏫 NSTI Allahabad Portal")
    st.write("Welcome 👋 Explore services below")

    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    🌐 [Official Website](https://nstiwallahabad.dgt.gov.in/)  
    📚 [View Courses](https://nstiwallahabad.dgt.gov.in/en/course-offered)  
    """)

    st.markdown("---")
    st.subheader("🎯 Student Services")

    col1, col2, col3, col4 = st.columns(4)

    # ---------- COURSES ----------
    if col1.button("💻 Courses"):
        st.success("""
📚 Available Courses:
- COPA (Computer Operator & Programming Assistant)
- CSA (Computer Software Applications)
- AIPA (Advanced IT & Cloud)
- EM (Electronics Mechanic)
- FDT (Fashion Design)

👉 https://nstiwallahabad.dgt.gov.in/en/course-offered
""")

    # ---------- HOSTEL ----------
    if col2.button("🏠 Hostel"):
        st.info("""
🏠 Hostel Facility:
- Girls hostel available
- Food & security
- Limited seats

👉 https://nstiwallahabad.dgt.gov.in/en/manage-hostel
""")

    # ---------- FEES ----------
    if col3.button("💰 Fees"):
        st.warning("""
💰 Fee Structure (Approx):

🔹 CTS Courses:
- ₹550 – ₹2000 (varies by trade)

🔹 CITS Courses:
- ₹600 – ₹2000 (add in Hostel Room fees)

💡 Government institutes have very low fees

👉 https://nstiwallahabad.dgt.gov.in/en/fee-structure
""")

    # ---------- CONTACT ----------
    if col4.button("📞 Contact"):
        st.markdown("""
📞 Contact NSTI Prayagraj

👉 https://nstiwallahabad.dgt.gov.in/en/about-us
""")

    st.markdown("---")
    st.subheader("📢 Admission Status")

    st.info("""
🎓 **CTS Admission:** Open May to June  
👨‍🏫 **CITS Admission:** Through AICET Entrance Exam (Registration Portal open 18 April 2026) 
""")

# ---------- ELIGIBILITY + CHECKER ----------
elif page == "🎓 Eligibility & Checker":

    st.title("🎓 Eligibility & Checker")

    tab1, tab2 = st.tabs(["Eligibility", "Check Yourself"])

    with tab1:
        st.subheader("CTS (Craftsmen Training Scheme)")
        st.write("""
        ✔ Qualification: 10th Pass  
        ✔ Duration: 1 Year  
        ✔ Admission: Merit Based  
        """)

        st.subheader("CITS (Instructor Training)")
        st.write("""
        ✔ Qualification: ITI / Diploma / Degree  
        ✔ Duration: 1 Year  
        ✔ Entrance Exam: AICET  
        """)

    with tab2:
        q = st.selectbox("Select Qualification", [
            "10th Pass", "12th Pass", "ITI", "Diploma", "Degree"
        ])

        if st.button("Check Eligibility"):
            if q == "10th Pass":
                st.success("✅ Eligible for CTS")
            elif q in ["ITI", "Diploma", "Degree"]:
                st.success("✅ Eligible for CITS")
            else:
                st.warning("⚠️ Limited options")

# ---------- DOCUMENTS ----------
elif page == "📄 Documents":

    st.title("📄 Documents Required")

    tab1, tab2 = st.tabs(["CTS", "CITS"])

    with tab1:
        st.subheader("CTS Documents")
        category = st.selectbox("Select Category", ["General", "OBC", "SC/ST", "EWS"])

        st.markdown("""
✔ 10th Marksheet  
✔ Aadhaar Card  
✔ Photos  
✔ Domicile  
""")

        if category != "General":
            st.info(f"✔ {category} Certificate required")

    with tab2:
        st.subheader("CITS Documents")
        category = st.selectbox("Select Category ", ["General", "OBC", "SC/ST", "EWS"])

        st.markdown("""
✔ ITI/Diploma/Degree  
✔ Aadhaar Card  
✔ Photos  
✔ Domicile  
""")

        if category != "General":
            st.info(f"✔ {category} Certificate required")

# ---------- AI ASSISTANT ----------
elif page == "🤖 AI Assistant":

    st.title("🤖 NSTI Smart Assistant")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    def bot_reply(user):
        user = user.lower()

        if "course" in user:
            return """📚 Courses:
COPA, CSA, AIPA, EM, FDT

👉 https://nstiwallahabad.dgt.gov.in/en/course-offered"""

        elif "hostel" in user:
            return """🏠 Hostel Info:
Girls hostel available, food + security

👉 https://nstiwallahabad.dgt.gov.in/"""

        elif "contact" in user:
            return "📞 https://nstiwallahabad.dgt.gov.in/en/about-us"
        
        elif "teacher" in user or "faculty" in user:
            return "👩‍🏫 Highly experienced instructors are available."

        elif "placement" in user:
            return "💼 Placement assistance available"

        elif "exam" in user:
            return "📝 Semester exams + practical"
        
        elif "form" in user: 
            return "📝 Forms are available online or at the institute."

        elif "admission" in user:
            return "🎓 CTS: Merit | CITS: AICET Entrance exam"
        
        elif "seat" in user:
            return "⚠️ Seats are limited depending on course."

        elif "documents" in user:
            return "📄 Marksheet, Aadhaar, Photos, Category Certificate"

        elif "location" in user:
            return "📍 NSTI Prayagraj - New Katra"
        
        elif "timing" in user:
            return "⏰ Institute timing: 9 AM to 5 PM"
        
        elif "bye" in user:
            return "👋 Goodbye! Visit again!"

        else:
            return "Ask about courses, hostel, admission, documents, contact"

    user_input = st.chat_input("Ask anything about NSTI...")

    if user_input:
        response = bot_reply(user_input)
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

    for sender, msg in st.session_state.chat:
        st.write(f"**{sender}:** {msg}")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("© 2026 NSTI Prayagraj Smart Portal 🚀")