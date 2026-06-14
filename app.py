import streamlit as st
from recommender import CourseRecommender

st.set_page_config(
    page_title="Course Recommender",
    layout="wide"
)

# CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}
[data-testid="stHeader"]{
    background: transparent;
}
h1,h2,h3{
    color:white !important;
}
.stTextInput label,
.stSelectbox label{
    color:white !important;
    font-weight:600;
    font-size:16px !important;
}
.stButton > button{
    background: linear-gradient(90deg, #2563eb, #06b6d4);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:600;
    width:100%;
}
hr{
    border:1px solid rgba(255,255,255,0.15);
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style='
    text-align:center;
    padding:25px;
    background:rgba(255,255,255,0.95);
    border-radius:18px;
    box-shadow:0 8px 25px rgba(0,0,0,0.2);
    margin-bottom:25px;
'>
    <div style='font-size:40px; font-weight:800; color:#0f172a;'>
        🎯 AI Course Recommender
    </div>
    <div style='color:#64748b; font-size:15px; margin-top:10px; letter-spacing:1px;'>
        ML-Powered Personalized Learning Path
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load model
recommender = CourseRecommender("coursera_dataset.csv")

# Input
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
    top_n = st.slider("Number of recommendations", 3, 10, 5)

st.markdown("---")

# Button
if st.button("🚀 Get My Recommendations"):

    if not user_skills_input:
        st.warning("⚠️ Please enter at least one skill!")

    else:
        user_skills = [s.strip() for s in user_skills_input.split(",")]

        with st.spinner("Finding best courses for you..."):
            recommendations = recommender.recommend(user_skills, user_level, top_n)

        if recommendations.empty:
            st.error("No courses found! Try different skills or level.")

        else:
            st.markdown(
                f"<h3 style='color:white;'>🎓 Top {top_n} Recommended Courses for You</h3>",
                unsafe_allow_html=True
            )

            for idx, row in recommendations.iterrows():
                st.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.97);
                    padding:20px;
                    border-radius:15px;
                    margin-bottom:18px;
                    border-left:5px solid #2563eb;
                    box-shadow:0 8px 20px rgba(0,0,0,0.15);
                ">
                    <div style="font-size:20px; font-weight:700; color:#0f172a;">
                        📚 {row['Title']}
                    </div>
                    <div style="color:#64748b; margin-top:8px; font-size:14px;">
                        🏛️ {row['Organization']} &nbsp;|&nbsp;
                        📊 {row['Difficulty']} &nbsp;|&nbsp;
                        ⭐ {row['Ratings']} &nbsp;|&nbsp;
                        ⏱️ {row['Duration']}
                    </div>
                    <div style="
                        margin-top:12px;
                        display:inline-block;
                        background:#dcfce7;
                        color:#15803d;
                        padding:6px 12px;
                        border-radius:20px;
                        font-size:13px;
                        font-weight:700;
                    ">
                        🎯 Match Score: {row['similarity_score']:.2f}
                    </div>
                    <div style="color:#475569; margin-top:12px; font-size:13px;">
                        🔧 Skills: {row['Skills'][:100]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div style="text-align:center; color:#e2e8f0; font-size:14px; padding:15px;">
    ⚡ Developed by
    <span style="color:#38bdf8; font-weight:bold;">Ashwini Parmar</span>
    • Data Science Portfolio Project
</div>
""", unsafe_allow_html=True)
