import streamlit as st

st.set_page_config(page_title="GPA Calculator", page_icon="🎓")

st.title("GPA Calculator 🎓")

st.write("Enter your subjects and their grades:")

num_courses = st.number_input("Number of subjects", min_value=1, step=1)

grades = []
credits = []

for i in range(int(num_courses)):
    grade = st.number_input(f"Grade for subject {i+1} (0-20):", min_value=0.0, max_value=20.0, step=0.1)
    credit = st.number_input(f"Credits for subject {i+1}:", min_value=1.0, step=1.0)
    grades.append(grade)
    credits.append(credit)

if st.button("Calculate GPA"):
    total_weighted = sum([g * c for g, c in zip(grades, credits)])
    total_credits = sum(credits)
    gpa = total_weighted / total_credits if total_credits else 0
    st.success(f"Your GPA is: {round(gpa, 2)} / 20")
  
