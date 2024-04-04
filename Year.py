import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
def plot_sentiment_trends(filtered_data):
    filtered_data['corpus_edition_date'] = pd.to_datetime(filtered_data['corpus_edition_date'])
    sentiment_counts_by_year_and_school = filtered_data.groupby([filtered_data['corpus_edition_date'].dt.year, 'school', 'SentimentLabel']).size().unstack()
    st.set_option('deprecation.showPyplotGlobalUse', False) 
    plt.figure(figsize=(10, 6))
    for year in sentiment_counts_by_year_and_school.index.levels[0]:

        year_data = sentiment_counts_by_year_and_school.loc[year]

        for school in year_data.index:
            plt.plot(year_data.columns, year_data.loc[school], marker='o', label=school)
    plt.title("Sentiment Trends of Schools ")
    plt.xlabel('Sentiment Label')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='School', bbox_to_anchor=(1.05, 1), loc='upper left')
    st.pyplot()
def plot_emotion_distribution(filtered_data):
    emotion_counts = filtered_data['emotion_label'].value_counts()
    fig = px.bar(x=emotion_counts.index, y=emotion_counts.values, labels={'x': 'Emotion Label', 'y': 'Count'})
    st.subheader("Emotion Label Distribution:")
    st.plotly_chart(fig)
def plot_sentiment_by_school(filtered_data):
    sentiment_counts_by_school = filtered_data.groupby(['school', 'SentimentLabel']).size().unstack(fill_value=0)
    fig = px.bar(sentiment_counts_by_school, barmode='group')
    st.subheader("Sentiment Distribution by School:")
    st.plotly_chart(fig)
def plot_compound_score_distribution(filtered_data):
    plt.figure(figsize=(8, 6))
    sns.histplot(filtered_data["CompoundScore"], bins=20, kde=True)
    plt.title("Distribution of Compound Scores")
    plt.xlabel("Compound Score")
    plt.ylabel("Density")
    st.pyplot()
  
    st.subheader("Sentiment Label Distribution:")
    sentiment_counts_filtered = filtered_data['SentimentLabel'].value_counts()
    fig = px.bar(x=sentiment_counts_filtered.index, y=sentiment_counts_filtered.values, labels={'x': 'Sentiment Label', 'y': 'Count'})
    st.plotly_chart(fig)
df = pd.read_csv("final.csv")
year_column = 'corpus_edition_date'
selected_year_range = st.slider("Select Year Range", min_value=1970, max_value=2016, value=(1970, 2016))
filtered_data = df[df[year_column].between(selected_year_range[0], selected_year_range[1])]
st.write(filtered_data)
plot_sentiment_trends(filtered_data)
plot_emotion_distribution(filtered_data)
plot_sentiment_by_school(filtered_data)
plot_compound_score_distribution(filtered_data)

