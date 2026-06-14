import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CourseRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        
        # Drop unnecessary columns
        self.df = self.df.drop(['Unnamed: 0', 'course_url', 
                                'course_students_enrolled', 
                                'course_description'], axis=1, errors='ignore')
        
        # TF-IDF on Skills
        self.vectorizer = TfidfVectorizer()
        self.skill_vectors = self.vectorizer.fit_transform(self.df['Skills'])
    
    def recommend(self, user_skills, user_level, top_n=5):
        user_skill_string = ', '.join(user_skills)
        user_vector = self.vectorizer.transform([user_skill_string])
        similarities = cosine_similarity(user_vector, self.skill_vectors).flatten()
        
        result = self.df.copy()
        result['similarity_score'] = similarities
        
        # Filter by difficulty
        filtered = result[result['Difficulty'] == user_level]
        top = filtered.sort_values('similarity_score', ascending=False).head(top_n)
        
        return top[['Title', 'Organization', 'Skills', 
                    'Ratings', 'Difficulty', 'Duration', 'similarity_score']]
    
    def get_levels(self):
        return self.df['Difficulty'].dropna().unique().tolist()