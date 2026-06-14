![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![ML](https://img.shields.io/badge/ML-TF--IDF%20%2B%20Cosine%20Similarity-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

# 🎯 AI Course Recommender — Powered by Coursera Data

## 🌐 Live Demo
👉 [Launch App](https://courserecommendor-z3tzl9ry7gzn8rmfrxpyue.streamlit.app/)

---

## 📌 Overview
An ML-powered web application that recommends personalized Coursera courses based on a user's current skills and experience level.

Using real Coursera course data and TF-IDF + Cosine Similarity, the app finds the most relevant courses matching the user's skill profile — helping learners discover the best next step in their learning journey.

---

## 🎯 Features
- ✅ Personalized course recommendations based on user skills
- ✅ Filter by difficulty level — Beginner, Intermediate, Advanced
- ✅ Real Coursera dataset — 623 courses from top organizations
- ✅ Match score for each recommendation
- ✅ Clean, modern dark UI built with Streamlit

---

## 🧠 How It Works
User enters skills + level
↓
TF-IDF converts skills to vectors
↓
Cosine Similarity — match user skills with course skills
↓
Filter by difficulty level
↓
Top N most relevant courses recommended!
---

## 🤖 ML Technique Used

| Technique | Purpose |
|---|---|
| **TF-IDF Vectorization** | Convert skills text to numerical vectors |
| **Cosine Similarity** | Measure similarity between user skills and course skills |
| **Difficulty Filtering** | Filter courses by user's experience level |

**Why TF-IDF + Cosine Similarity?**
- Same technique used by Netflix, Amazon recommendation systems
- Handles text data efficiently
- Gives interpretable similarity scores (0 to 1)

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| ML Technique | TF-IDF + Cosine Similarity |
| ML Framework | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Web App | Streamlit |
| Deployment | Streamlit Cloud |

---

## 📂 Dataset
- **Source:** Coursera Course Dataset (Kaggle)
- **Records:** 623 real Coursera courses
- **Organizations:** Google, IBM, DeepLearning.AI, Meta and more
- **Features:** Title, Skills, Difficulty, Ratings, Duration, Organization

---

## 📁 Project Structure
learning_path_recommender/

│

├── app.py                              # Streamlit web application

├── recommender.py                      # ML recommendation logic

├── coursera_course_dataset_v3.csv      # Real Coursera dataset

├── coursera_recommender.ipynb          # Jupyter notebook — full analysis

└── requirements.txt                    # Dependencies

---

## 🚀 Run Locally

```bash
git clone https://github.com/Ashwini1813/learning_path_recommender.git
cd learning_path_recommender
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎓 Learning Outcomes
- TF-IDF Vectorization for text data
- Cosine Similarity for recommendation systems
- Real-world dataset cleaning and preprocessing
- End-to-end ML project deployment

---

## 👩‍💻 Developer
**Ashwini Parmar** 
