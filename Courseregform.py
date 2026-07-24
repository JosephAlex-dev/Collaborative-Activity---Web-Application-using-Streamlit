import streamlit as st
import time
import pandas as pd

st.set_page_config(page_title="Course Registration", page_icon="🎓", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(-45deg, #1a2a6c, #2c5364, #0f2027, #16324f);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1 {
    color: #ffffff !important;
    text-align: center;
    font-weight: 700;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    color: #cfe8f3;
    font-size: 16px;
    margin-bottom: 25px;
}

div[data-testid="stForm"] {
    background-color: rgba(255, 255, 255, 0.97);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.3);
}

div[data-testid="stForm"] h3 {
    color: #1a2a6c !important;
    border-left: 5px solid #f9b234;
    padding-left: 10px;
}

div[data-testid="stForm"] label p {
    color: #1a2a6c !important;
    font-weight: 600;
}

div[data-testid="stForm"] input,
div[data-testid="stForm"] textarea {
    background-color: #f5f6fa !important;
    color: #1a2a6c !important;
    border: 1px solid #ccd6e0 !important;
    border-radius: 8px !important;
    transition: 0.2s;
}

div[data-testid="stForm"] input:focus,
div[data-testid="stForm"] textarea:focus {
    border: 1px solid #f9b234 !important;
    box-shadow: 0 0 0 2px rgba(249,178,52,0.25) !important;
}

div[data-testid="stForm"] div[data-baseweb="select"] > div {
    background-color: #f5f6fa !important;
    color: #1a2a6c !important;
    border: 1px solid #ccd6e0 !important;
    border-radius: 8px !important;
}

div[data-testid="stForm"] div[data-baseweb="select"] span {
    color: #1a2a6c !important;
}

div[data-testid="stFileUploaderDropzone"] {
    background-color: #f5f6fa !important;
    border: 1px dashed #f9b234 !important;
    border-radius: 10px !important;
}

div[data-testid="stFileUploaderDropzone"] * {
    color: #1a2a6c !important;
}

.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: #e0721a !important;
}

.stButton>button {
    background: linear-gradient(90deg, #f9b234, #e0721a);
    color: #ffffff !important;
    border-radius: 10px;
    padding: 12px 24px;
    font-weight: 700;
    border: none;
    width: 100%;
    transition: 0.2s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #e0721a, #f9b234);
    color: #ffffff !important;
    transform: translateY(-2px);
    box-shadow: 0px 4px 15px rgba(224,114,26,0.5);
}

[data-testid="stMetricValue"] {
    color: #1a2a6c !important;
}

section[data-testid="stSidebar"] {
    background-color: #0f2027;
}

section[data-testid="stSidebar"] * {
    color: #cfe8f3 !important;
}

.footer-note {
    text-align: center;
    color: #cfe8f3;
    font-size: 13px;
    margin-top: 30px;
    opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)

if "registration_count" not in st.session_state:
    st.session_state.registration_count = 0

with st.sidebar:
    st.header("📋 Registration Desk")
    st.write("Semester intake is currently open.")
    st.metric("Students Registered Today", st.session_state.registration_count)
    st.divider()
    with st.expander("Why do we need this info?"):
        st.write("Personal details verify identity, academic details assign your batch, and course selection determines your fee and timetable.")
    with st.expander("Fee Structure"):
        st.write("₹3000 per course, billed at the time of registration.")

st.title("🎓 Course Registration Form")
st.markdown('<p class="subtitle">Fill in your details to register for the upcoming semester</p>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📝 New Registration", "ℹ️ Instructions"])

with tab2:
    st.write("1. Fill in all personal and academic details.")
    st.write("2. Select at least one course.")
    st.write("3. Upload your ID proof if required.")
    st.write("4. Accept Terms and Conditions before submitting.")

with tab1:
    with st.form("registration_form", clear_on_submit=True):
        st.subheader("Personal Details")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="Enter your full name", help="As it appears on your ID proof")
            phone = st.text_input("Phone Number", placeholder="10-digit mobile number", help="Used for registration confirmation SMS")
            gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        with col2:
            email = st.text_input("Email Address", placeholder="you@example.com", help="University email preferred")
            dob = st.date_input("Date of Birth")
            age = st.number_input("Age", min_value=16, max_value=60, step=1)

        mode = st.radio("Mode of Study", ["Online", "Offline", "Hybrid"], horizontal=True)

        st.divider()
        st.subheader("Academic Details")
        col3, col4 = st.columns(2)
        with col3:
            department = st.selectbox(
                "Department",
                ["Computer Applications", "Commerce", "Psychology", "Economics", "Data Science"]
            )
        with col4:
            semester = st.selectbox(
                "Semester",
                ["1", "2", "3", "4", "5", "6"]
            )

        courses = st.multiselect(
            "Select Courses",
            ["Python Programming", "Web Development", "Data Structures",
             "Cloud Computing", "AI Fundamentals", "Database Systems"],
            help="You can select multiple courses"
        )

        credits = st.slider("Preferred Credit Load", min_value=12, max_value=24, value=18, step=2)

        address = st.text_area("Address", placeholder="Enter your current address")

        id_proof = st.file_uploader("Upload ID Proof", type=["pdf", "jpg", "png"])

        st.divider()
        terms = st.checkbox("I agree to the Terms and Conditions")

        submitted = st.form_submit_button("Register Now")

    if submitted:
        if not name or not email or not phone or not courses:
            st.error("Please fill all required fields and select at least one course.")
        elif not terms:
            st.warning("Please accept the Terms and Conditions.")
        else:
            progress = st.progress(0, text="Validating details...")
            for pct, label in [(30, "Validating details..."), (60, "Checking course availability..."), (90, "Finalizing registration..."), (100, "Done!")]:
                time.sleep(0.4)
                progress.progress(pct, text=label)
            time.sleep(0.3)
            progress.empty()

            st.session_state.registration_count += 1
            fee_per_course = 3000
            total_fee = len(courses) * fee_per_course

            st.success("Registration Successful!")
            st.balloons()

            st.markdown("### Registration Summary")
            colA, colB = st.columns(2)
            with colA:
                st.write("Name:", name)
                st.write("Email:", email)
                st.write("Phone:", phone)
                st.write("Date of Birth:", dob)
                st.write("Age:", age)
                st.write("Gender:", gender)
            with colB:
                st.write("Department:", department)
                st.write("Semester:", semester)
                st.write("Mode of Study:", mode)
                st.write("Credit Load:", credits)
                st.write("Address:", address)

            st.markdown("#### Fee Breakdown")
            fee_table = pd.DataFrame({
                "Course": courses,
                "Fee (₹)": [fee_per_course] * len(courses)
            })
            st.table(fee_table)

            colM1, colM2 = st.columns(2)
            with colM1:
                st.metric("Total Courses", len(courses))
            with colM2:
                st.metric("Total Fee", f"₹{total_fee}")

            if id_proof is not None:
                st.info(f"ID Proof Uploaded: {id_proof.name}")

st.markdown('<p class="footer-note">Dekho Team • Course Registration Demo • Advanced Python</p>', unsafe_allow_html=True)
