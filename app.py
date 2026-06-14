import streamlit as st
from recommender import CourseRecommender

st.set_page_config(
    page_title="Course Recommender",
    layout="wide"
)

# Professional Styling
st.markdown("""
<style>
    .stApp {
        background: #f8fafc;
    }

    .stTextInput label,
    .stSelectbox label,
    .stMultiSelect label {
        color: #1e293b !important;
        font-size: 16px !important;
        font-weight: 600;
    }

    .stTextInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: white !important;
    }

    .stButton > button {
        background: #2563eb;
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: #1d4ed8;
    }

    h1, h2, h3 {
        color: #0f172a !important;
    }

    hr {
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("""
<div style='
    text-align:center;
    padding:25px;
    background:white;
    border-radius:15px;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
'>
    <div style='
        font-size:38px;
        font-weight:700;
        color:#0f172a;
    '>
        🎯 AI Course Recommender
    </div>

    <div style='
        color:#64748b;
        font-size:15px;
        margin-top:10px;
        letter-spacing:1px;
    '>
        Personalized Course Recommendations Using Machine Learning
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load Recommender
recommender = CourseRecommender("coursera_dataset.csv")

# Input Section
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💡 Your Current Skills")
    user_skills_input = st.text_input(
        "Enter your skills (comma separated)",
        placeholder="e.g. python, sql, machine learning"
    )

with col2:
    st.markdown("### 📊 Your Level")
    user_level = st.selectbox(
        "Select your current level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    top_n = st.slider(
        "Number of recommendations",
        3,
        10,
        5
    )

st.markdown("---")

# Recommend Button
if st.button("🚀 Get My Recommendations"):

    if not user_skills_input:
        st.warning("⚠️ Please enter at least one skill!")
    else:

        user_skills = [
            s.strip()
            for s in user_skills_input.split(",")
        ]

        with st.spinner("Finding best courses for you..."):
            recommendations = recommender.recommend(
                user_skills,
                user_level,
                top_n
            )

        if recommendations.empty:
            st.error(
                "No courses found! Try different skills or level."
            )

        else:
            st.markdown(
                f"### 🎓 Top {top_n} Recommended Courses for You"
            )

            for idx, row in recommendations.iterrows():

                st.markdown(f"""
                <div style='
                    background:white;
                    padding:20px;
                    border-radius:12px;
                    margin-bottom:15px;
                    border:1px solid #e2e8f0;
                    box-shadow:0 2px 8px rgba(0,0,0,0.05);
                '>

                    <div style='
                        font-size:20px;
                        font-weight:700;
                        color:#0f172a;
                    '>
                        📚 {row['Title']}
                    </div>

                    <div style='
                        color:#64748b;
                        margin-top:8px;
                        font-size:14px;
                    '>
                        🏛️ {row['Organization']} |
                        📊 {row['Difficulty']} |
                        ⭐ {row['Ratings']} |
                        ⏱️ {row['Duration']}
                    </div>

                    <div style='
                        margin-top:10px;
                        display:inline-block;
                        background:#dbeafe;
                        color:#1d4ed8;
                        padding:6px 12px;
                        border-radius:20px;
                        font-size:13px;
                        font-weight:600;
                    '>
                        🎯 Match Score:
                        {row['similarity_score']:.2f}
                    </div>

                    <div style='
                        color:#475569;
                        margin-top:12px;
                        font-size:13px;
                    '>
                        🔧 Skills:
                        {row['Skills'][:100]}...
                    </div>

                </div>
                """, unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("""
<div style='
    text-align:center;
    color:#64748b;
    font-size:14px;
    padding:15px;
'>
    ⚡ Developed by
    <b style='color:#2563eb;'>Ashwini Parmar</b>
    • Data Science Portfolio Project
</div>
""", unsafe_allow_html=True)
