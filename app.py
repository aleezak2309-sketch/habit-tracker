import streamlit as st
from datetime import date

st.set_page_config(page_title="Coding Practice Tracker", page_icon="💻", layout="wide")

st.markdown("""
...
<style>
.stApp {
    background: linear-gradient(135deg, #1a0b2e, #0f1b3c);
    color: #e6e6fa;
}
.banner {
    background: linear-gradient(90deg, #6a0dad, #2e5cff);
    padding: 0.8rem 1rem;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 20px rgba(106, 13, 173, 0.4);
}
.banner h1 {
    color: white;
    font-size: 1.4rem;
    margin: 0;
}
.banner p {
    color: #d8c7ff;
    margin-top: 0.1rem;
    font-size: 0.85rem;
}
.navbar {
    display: flex;
    justify-content: center;
    gap: 1.2rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}
.navbar a {
    color: #c3a6ff;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.85rem;
    padding: 0.3rem 0.6rem;
    border: 1px solid #6a0dad;
    border-radius: 6px;
}
.navbar a:hover {
    background-color: #6a0dad;
    color: white;
}
div.stButton > button {
    background: linear-gradient(90deg, #6a0dad, #2e5cff);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.2rem;
    font-weight: 600;
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #7d1fc2, #4a7bff);
    color: white;
}
h2, h3 {
    color: #c3a6ff;
}
</style>

<div class="banner">
    <h1>Coding Practice Tracker</h1>
    <p>Log it. Review it. Master it.</p>
</div>

<div class="navbar">
    <a href="#add-topic">Add Topic</a>
    <a href="#log-question">Log Question</a>
    <a href="#view-topics">View Topics</a>
    <a href="#delete-topic">Delete Topic</a>
    <a href="#edit-question">Edit Question</a>
    <a href="#search-questions">Search</a>
    <a href="#topics-sorted-by-most-solved">Sorted</a>
    <a href="#personal-best">Personal Best</a>
    <a href="#topic-mastery">Topic Mastery</a>
</div>
""", unsafe_allow_html=True)
