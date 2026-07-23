import streamlit as st

st.title("Course Registration Form")

with st.form("registration_form"):
    name = st.text_input("Full Name", placeholder="Enter your full name")
    email = st.text_input("Email Address", placeholder="you@example.com")

    department = st.selectbox(
        "Department",
        ["Computer Applications", "Commerce", "Psychology", "Economics", "Data Science"]
    )

    semester = st.selectbox(
        "Semester",
        ["1", "2", "3", "4", "5", "6"]
    )

    courses = st.multiselect(
        "Select Courses",
        ["Python Programming", "Web Development", "Data Structures", "Cloud Computing", "AI Fundamentals", "Database Systems"]
    )

    submitted = st.form_submit_button("Register")

if submitted:
    if not name or not email or not courses:
        st.error("Please fill all fields and select at least one course.")
    else:
        st.success("Registration Successful!")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Department:", department)
        st.write("Semester:", semester)
        st.write("Courses Selected:", ", ".join(courses))