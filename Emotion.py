import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("final.csv")
st.title("Sentiment Analysis of Cultural Heritage Texts")

st.sidebar.title("Emotion Label Selection")
selected_emotions = st.sidebar.multiselect("Select Emotion Labels", df['emotion_label'].unique(), help="Filter the data by selecting emotion labels")

filtered_data_emotions = df[df['emotion_label'].isin(selected_emotions)]

if selected_emotions:

    st.subheader("Emotion Label Distribution:")
    emotion_counts_filtered = filtered_data_emotions['emotion_label'].value_counts()
    fig = px.pie(names=emotion_counts_filtered.index, values=emotion_counts_filtered.values)
    st.plotly_chart(fig)

    st.subheader("Emotion Label Distribution Across Schools:")
    school_emotion_counts = filtered_data_emotions.groupby(['school', 'emotion_label']).size().unstack(fill_value=0)
    fig = px.bar(school_emotion_counts, barmode='group')
    st.plotly_chart(fig)

    st.subheader("Sentiment Trends Across Authors:")
    author_sentiment_counts = filtered_data_emotions.groupby(['author', 'SentimentLabel']).size().unstack(fill_value=0)
    fig = px.bar(author_sentiment_counts, barmode='group')
    st.plotly_chart(fig)
    
    st.subheader("Average CompoundScore by School:")
    avg_compound_score_by_school = filtered_data_emotions.groupby('school')['CompoundScore'].mean().reset_index()
    fig = px.bar(avg_compound_score_by_school, x='school', y='CompoundScore', labels={'school': 'School', 'CompoundScore': 'Average CompoundScore'})
    fig.update_layout(xaxis_title="School", yaxis_title="Average CompoundScore")
    st.plotly_chart(fig)

    

else:
    st.info("Please select emotion labels to see the graphs for emotions.")
