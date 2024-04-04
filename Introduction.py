import streamlit as st

st.title("Exploring Sentiment Trends of philosophers Texts Through Data Visualization")
st.write("This app provides insights into the sentiments expressed across a diverse range of philosophical texts from various schools of thought.")
st.header("History  of Philosophy Dataset ")
st.write("Dataset link :- https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy ")
st.sidebar.title("Emotion Label Selection")
st.sidebar.write("Use the sidebar to select emotion labels for filtering the data.")

st.header("Represented Schools of Philosophy")
st.write("Explore the diverse spectrum of philosophical traditions represented in this app, each offering unique perspectives on the fundamental questions of existence and knowledge.")

schools_info = {
    "Plato": "The teachings of Plato, a foundational figure in Western philosophy, emphasize the pursuit of truth, justice, and the ideal forms.",
    "Aristotle": "Aristotle, a student of Plato, explored diverse topics ranging from metaphysics and ethics to logic and politics, shaping Western thought for centuries.",
    "Rationalism": "Rationalist philosophers prioritize reason and innate knowledge as the primary sources of understanding, advocating for deductive reasoning and abstract thought.",
    "Empiricism": "Empiricists assert that knowledge arises primarily from sensory experience and observation, emphasizing empirical evidence over innate ideas.",
    "German Idealism": "German Idealism, notably championed by figures like Immanuel Kant and Georg Wilhelm Friedrich Hegel, explores the nature of reality, consciousness, and freedom.",
    "Communism": "Philosophical foundations of communism, as articulated by Karl Marx and Friedrich Engels, advocate for the abolition of private property and the establishment of a classless society.",
    "Capitalism": "Capitalist philosophy emphasizes individual rights, free markets, and private ownership of property as essential components of economic and social organization.",
    "Phenomenology": "Phenomenology, developed by Edmund Husserl and expanded upon by thinkers like Martin Heidegger, investigates the structures of human consciousness and the phenomena of lived experience.",
    "Continental Philosophy": "Continental philosophy encompasses a diverse range of philosophical traditions originating primarily in Europe, focusing on existentialism, hermeneutics, and critical theory.",
    "Analytic Philosophy": "Analytic philosophy emphasizes clarity of language, logical analysis, and rigorous argumentation, with roots in the work of figures like Bertrand Russell and Ludwig Wittgenstein."
}

for school, info in schools_info.items():
    st.subheader(school)
    st.write(info)

st.header("Analyzing Sentiments Across Texts")
st.write("In this app, you can explore sentiment analysis results across different philosophical texts and schools of thought. Dive into the nuances of philosophical discourse and uncover the emotional tones underlying these profound intellectual explorations!")
