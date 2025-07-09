import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re

df = pd.read_csv("twitter_training.csv", header=None, names=['id', 'entity', 'sentiment', 'text'])
def clean(text):
    if not isinstance(text, str):
        return ''
    return re.sub(r"http\S+|@\w+|#|[^A-Za-z\s]", '', text).lower()
df['clean_text'] = df['text'].apply(clean)

sentiment_counts = df['sentiment'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=sns.color_palette("Set2"))
plt.title("Sentiment Distribution (Pie Chart)")
plt.savefig("visuals/sentiment_pie.png")
plt.show()

top5 = df['entity'].value_counts().nlargest(5).index
plt.figure(figsize=(8, 5))
sns.countplot(data=df[df['entity'].isin(top5)], x='entity', hue='sentiment', palette='Set1')
plt.title("Sentiment per Top 5 Entities")
plt.tight_layout()
plt.savefig("visuals/sentiment_per_entity.png")
plt.show()

top_entities = df['entity'].value_counts().nlargest(10)
plt.figure(figsize=(8, 5))
sns.barplot(y=top_entities.index, x=top_entities.values, palette='viridis')
plt.title("Top 10 Most Discussed Brands")
plt.xlabel("Tweet Count")
plt.tight_layout()
plt.savefig("visuals/top_entities.png")
plt.show()

pos = " ".join(df[df['sentiment'] == 'Positive']['clean_text'])
neg = " ".join(df[df['sentiment'] == 'Negative']['clean_text'])
fig, axs = plt.subplots(1, 2, figsize=(14, 6))
axs[0].imshow(WordCloud(background_color='white', colormap='Greens').generate(pos))
axs[0].set_title("Positive Tweets")
axs[0].axis('off')
axs[1].imshow(WordCloud(background_color='white', colormap='Reds').generate(neg))
axs[1].set_title("Negative Tweets")
axs[1].axis('off')
plt.tight_layout()
plt.savefig("visuals/wordclouds.png")
plt.show()