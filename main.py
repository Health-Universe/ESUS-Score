import streamlit as st

# App Title and Description
st.title("Embolic Stroke of Undetermined Source (ESUS) Criteria")
st.write("""
This app helps to determine if a patient meets the Embolic Stroke of Undetermined Source (ESUS) criteria.
ESUS is diagnosed when a patient has had an ischemic stroke, and the cause is not identified after a thorough diagnostic evaluation.
""")

# ESUS Criteria Inputs
st.subheader("Patient Criteria for ESUS")

age = st.number_input("Patient Age", min_value=0, max_value=120, step=1, value=65)

# Question 1: Large artery atherosclerosis
st.write("1. Large artery atherosclerosis exclusion")
atherosclerosis = st.selectbox(
    "Is there significant stenosis (≥50%) or occlusion in the relevant arteries?",
    ("No", "Yes")
)

# Question 2: Cardioembolism
st.write("2. Cardioembolism exclusion")
cardioembolism = st.selectbox(
    "Is there evidence of a high-risk cardioembolic source (e.g., atrial fibrillation, left ventricular thrombus, or recent myocardial infarction)?",
    ("No", "Yes")
)

# Question 3: Small vessel disease
st.write("3. Small vessel disease exclusion")
small_vessel_disease = st.selectbox(
    "Is there evidence of lacunar infarct consistent with small vessel disease (≤1.5 cm in diameter)?",
    ("No", "Yes")
)

# Calculate ESUS Result
if atherosclerosis == "No" and cardioembolism == "No" and small_vessel_disease == "No":
    st.success("The patient meets the criteria for Embolic Stroke of Undetermined Source (ESUS).")
else:
    st.warning("The patient does not meet the criteria for ESUS.")

# Additional Information Section
st.subheader("Additional Information")
st.write("""
Embolic Stroke of Undetermined Source (ESUS) refers to non-lacunar ischemic strokes that are not explained by cardioembolism, large artery atherosclerosis, or small vessel occlusion. It is crucial to rule out other possible causes before diagnosing ESUS.
""")
