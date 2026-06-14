import streamlit as st
from recommender import CourseRecommender

st.set_page_config(page_title="Course Recommender", layout="wide")

# Styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        }
        .stTextInput label, .stSelectbox label, .stMultiSelect label {
            color: #00d4ff !important;
            font-size: 16px !important;
        }
        .stButton > button {
            background: linear-gradient(90deg, #00d4ff, #7b2ff7);
            color: white;
            border: none;
            padding: 10px 30px;
            border-radius: 25px;
            font-size: 18px;
            font-weight: bold;
            width: 100%;
        }
        h1, h2, h3 {
            color: #00d4ff !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div style='
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #00d4ff;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        margin-top: 20px;
        font-family: "Segoe UI", sans-serif;
    '>
        🎯 AI Course Recommender
    </div>
    <div style='
        text-align: center;
        font-size: 16px;
        color: #a0b4c8;
        letter-spacing: 4px;
        margin-top: 8px;
        margin-bottom: 30px;
    '>
        ML-POWERED PERSONALIZED LEARNING PATH — POWERED BY COURSERA DATA
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load recommender
recommender = CourseRecommender("coursera_dataset.csv")

# Input section
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

# Recommend button
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
            st.markdown(f"### 🎓 Top {top_n} Recommended Courses for You")
            
            for idx, row in recommendations.iterrows():
                st.markdown(f"""
                <div style='
                    background: linear-gradient(135deg, #1a1a3e, #0d3b1e);
                    padding: 20px;
                    border-radius: 12px;
                    margin-bottom: 15px;
                    border-left: 4px solid #00d4ff;
                '>
                    <div style='font-size: 20px; font-weight: bold; color: #00d4ff;'>
                        📚 {row['Title']}
                    </div>
                    <div style='color: #a0b4c8; margin-top: 5px;'>
                        🏛️ {row['Organization']} &nbsp;|&nbsp; 
                        📊 {row['Difficulty']} &nbsp;|&nbsp; 
                        ⭐ {row['Ratings']} &nbsp;|&nbsp; 
                        ⏱️ {row['Duration']}
                    </div>
                    <div style='color: #7b2ff7; margin-top: 5px; font-size: 14px;'>
                        🎯 Match Score: {row['similarity_score']:.2f}
                    </div>
                    <div style='color: #a0b4c8; margin-top: 5px; font-size: 13px;'>
                        🔧 Skills: {row['Skills'][:100]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #a0b4c8; font-size: 14px;'>
    ⚡ Developed by <b style="color:#00d4ff;">Ashwini Parmar</b> | 
    Data Science Portfolio Project | Powered by Coursera Dataset
</div>
""", unsafe_allow_html=True)