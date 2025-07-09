# PRODIGY_DS_04
This project analyzes Twitter data to uncover public sentiment patterns toward various brands. It includes data cleaning, sentiment distribution analysis, entity-level insights, and visual word clouds. Built using Python, pandas, seaborn, and wordcloud.

## Objective
To explore and visualize sentiment patterns in social media data using real-world Twitter text labeled with sentiment (Positive, Negative, Neutral). This helps in understanding public opinion and brand perception.

## Dataset
- Source: [Twitter Entity Sentiment Analysis - Kaggle](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)
- File used: twitter_training.csv

## Tools Used
- Python
- pandas
- seaborn & matplotlib
- wordcloud
- Regular expressions (re)

## How to Run
1. Clone the repository and navigate to the folder  
2. Download the dataset from Kaggle and place twitter_training.csv in the root directory  
3. Run the script:
   python main.py
4. All plots will be shown and saved inside the visuals/ folder.

## Visualizations (Saved in /visuals folder)
- sentiment_pie.png : Pie chart of overall sentiment distribution.
- sentiment_per_entity.png : Bar plot of sentiment types for top 5 brands.
- top_entities.png : Horizontal bar chart of 10 most discussed entities.
- wordclouds.png : Word clouds showing most common words in positive & negative tweets.