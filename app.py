import streamlit as st
from datetime import date

st.set_page_config(page_title="Coding Practice Tracker", page_icon="📘", layout="wide")

st.markdown("""
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

if 'data' not in st.session_state:
    st.session_state.data = {}

# ================= ADD TOPIC =================
st.header("Add Topic")
topic_name = st.text_input('Enter a topic name', key='add_topic_input')

if st.button('Add Topic'):
    name = topic_name.strip().lower()
    if name == '':
        st.error('Please enter a name')
    elif name in st.session_state.data:
        st.error('Topic already exists')
    else:
        st.session_state.data[name] = []
        st.success(f'Added {name}')

# ================= LOG QUESTION =================
st.header("Log Question")

if not st.session_state.data:
    st.warning('Add a topic first!')
else:
    topic = st.selectbox('Choose a topic', list(st.session_state.data.keys()), key='log_topic_select')
    question = st.text_input('Question name', key='log_question_input')
    difficulty = st.selectbox('Difficulty', ['Easy', 'Medium', 'Hard'], key='log_difficulty_select')
    note = st.text_input('Notes (optional)', key='log_note_input')
    status = st.radio('Did you get it right or wrong?', ['right', 'wrong'], key='log_status_radio')
    solution = st.text_input('What went wrong / correct approach (optional)', key='log_solution_input') if status == 'wrong' else ''
    link = st.text_input('Link to the problem (optional)', key='log_link_input')

    if st.button('Log Question'):
        if question.strip() == '':
            st.error('Please enter a question name')
        else:
            duplicate = False
            for item in st.session_state.data[topic]:
                if item['name'] == question.strip():
                    duplicate = True
            if duplicate:
                st.error('Question already in data')
            else:
                st.session_state.data[topic].append({
                    'name': question.strip(),
                    'difficulty': difficulty,
                    'date': date.today().isoformat(),
                    'note': note,
                    'status': status,
                    'solution': solution,
                    'link': link
                })
                st.success(f'Logged {question} under {topic}')

# ================= VIEW TOPICS =================
st.header("View Topics")

if not st.session_state.data:
    st.write("No topics yet")
else:
    for topic, questions in st.session_state.data.items():
        st.subheader(f'{topic} ({len(questions)} solved)')
        for item in questions:
            note = item.get('note', '')
            solution = item.get('solution', '')
            link = item.get('link', '')
            status = item.get('status', '')

            line = f"**{item['name']}** — {item['difficulty']} — {item.get('date', '')} — {status}"
            st.write(line)
            if note != '':
                st.caption(f"note: {note}")
            if solution != '':
                st.caption(f"solution: {solution}")
            if link != '':
                st.write(f"[Problem link]({link})")

# ================= DELETE TOPIC =================
st.header("Delete Topic")

if not st.session_state.data:
    st.write("No topics to delete")
else:
    delete_choice = st.selectbox('Choose a topic to delete', list(st.session_state.data.keys()), key='delete_topic_select')
    if st.button('Delete Topic'):
        del st.session_state.data[delete_choice]
        st.success(f'{delete_choice} deleted')
        st.rerun()

# ================= EDIT QUESTION =================
st.header("Edit Question")

if not st.session_state.data:
    st.write("No topics yet")
else:
    edit_topic = st.selectbox('Choose a topic', list(st.session_state.data.keys()), key='edit_topic_select')
    questions_here = st.session_state.data[edit_topic]

    if not questions_here:
        st.write("No questions to edit in this topic")
    else:
        question_names = [q['name'] for q in questions_here]
        edit_choice = st.selectbox('Choose a question', question_names, key='edit_question_select')
        question_item = questions_here[question_names.index(edit_choice)]

        new_name = st.text_input('New name (leave blank to keep current)', key='edit_name_input')
        new_difficulty = st.selectbox('New difficulty (leave as is to keep current)', ['(keep current)', 'Easy', 'Medium', 'Hard'], key='edit_difficulty_select')

        if st.button('Save Changes'):
            if new_name.strip() != '':
                question_item['name'] = new_name.strip()
            if new_difficulty != '(keep current)':
                question_item['difficulty'] = new_difficulty
            st.success(f"Updated to {question_item['name']} ({question_item['difficulty']})")

# ================= SEARCH QUESTIONS =================
st.header("Search Questions")

keyword = st.text_input('Enter a keyword to search', key='search_input')

if st.button('Search'):
    found = False
    for topic, questions in st.session_state.data.items():
        for item in questions:
            if keyword.strip().lower() in item['name'].lower():
                st.write(f"Found: **{item['name']}** ({item['difficulty']}) — in {topic}")
                found = True
    if not found:
        st.write('No matches found')

# ================= SORT BY MOST SOLVED =================
st.header("Topics Sorted by Most Solved")

if not st.session_state.data:
    st.write("No topics yet")
else:
    sorted_topics = sorted(st.session_state.data.items(), key=lambda pair: len(pair[1]), reverse=True)
    for topic, questions in sorted_topics:
        st.write(f'{topic}: {len(questions)} solved')

# ================= PERSONAL BEST =================
st.header("Personal Best")

if not st.session_state.data:
    st.write("No data available")
else:
    date_counts = {}
    for topic, questions in st.session_state.data.items():
        for item in questions:
            d = item.get('date', '')
            if d == '':
                continue
            if d in date_counts:
                date_counts[d] += 1
            else:
                date_counts[d] = 1

    if date_counts:
        best_date = max(date_counts, key=date_counts.get)
        st.write(f"Your most productive day was **{best_date}** ({date_counts[best_date]} questions)")
    else:
        st.write("No dated questions yet")

# ================= TOPIC MASTERY =================
st.header("Topic Mastery")

if not st.session_state.data:
    st.write("No data available")
else:
    for topic, questions in st.session_state.data.items():
        if len(questions) == 0:
            st.write(f'{topic}: no questions logged yet')
            continue
        correct = 0
        for item in questions:
            if item.get('status', '') == 'right':
                correct += 1
        percent = (correct / len(questions)) * 100
        st.write(f'{topic}: {percent:.0f}% correct ({correct}/{len(questions)})')