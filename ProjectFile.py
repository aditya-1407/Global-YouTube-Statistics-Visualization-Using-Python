import numpy as np #linear algebra
import pandas as pd #importing CSV files, data processing
import seaborn as sns
import matplotlib.pyplot as plt

'''Data Loading'''
# dataFrame = pd.read_csv('Global YouTube Statistics.csv', encoding="ISO-8859-1")
# print(dataFrame.head())
# print(dataFrame.shape)
# print(dataFrame.info())
# print(dataFrame.describe())

'''Data Cleaning'''
# print(dataFrame.isnull().sum())

#Dropping Null Values
# dataFrame = dataFrame.dropna()
# print(dataFrame.isnull().sum())

#Dropping unrequired columns from data
# unrequired_columns = ['Abbreviation', 'created_month', 'created_date', 'Latitude', 'Longitude']
# df = dataFrame.drop(dataFrame[unrequired_columns], axis=1)
# print(df.info())

'''Data Visualization'''

#Top 10 Youtubers in terms of no. of Subs
# plt.figure(figsize=(10, 6))
# sns.set_theme(style='darkgrid')
# ax=sns.barplot(x='Youtuber', y='subscribers', data=df, order=df.sort_values('subscribers', ascending=False).Youtuber.iloc[:10], palette='magma')
# plt.xticks(rotation=45)
# ax.set_yticklabels([f'{int(label/1e6)}M' for label in ax.get_yticks()])
# plt.title('Top 10 Youtubers in terms of no. of Subscribers', fontsize=15, fontweight='bold')
# plt.show()

#Top 10 Youtubers in terms of Views
# plt.figure(figsize=(10, 6))
# sns.set_theme(style='darkgrid')
# ax=sns.barplot(x='Youtuber', y='video views', data=df, order=df.sort_values('video views', ascending=False).Youtuber.iloc[:10], palette='magma')
# plt.xticks(rotation=60)
# ax.set_yticklabels([f'{int(label/1e9)}B' for label in ax.get_yticks()])
# plt.title('Top 10 Youtubers in terms of Views(in billions)', fontsize=15, fontweight='bold')
# plt.show()

#Bar Plot
# plt.figure(figsize=(12, 6))
# sns.set_theme(style='darkgrid')
# sns.barplot(x='category', y='subscribers', data=df, errorbar=None)
# plt.xlabel('Category')
# plt.ylabel('Subscribers')
# plt.title('Channel Subscribers by its Category', fontsize=16, fontweight='bold')
# plt.xticks(rotation=90)
# plt.show()

#Count Plot
# plt.figure(figsize=(10, 6))
# df['channel_type'].value_counts().plot(kind='bar', color='orange')
# plt.xlabel('Channel Type')
# plt.ylabel('Count')
# plt.title('Channel Types Distribution')
# plt.xticks(rotation=45)
# plt.show()

#Line Plot
# plt.figure(figsize=(10, 6))
# sns.set_theme(style='darkgrid')
# sns.lineplot(x=df['subscribers'], y=df['video views'], alpha=0.5, color='purple', errorbar=None)
# plt.xlabel('Subscribers')
# plt.ylabel('Video Views')
# plt.title('Subs vs Video Views', fontsize=16, fontweight='bold')
# plt.show()

#Yealy Subs Line Plot
# df['created_year'] = df['created_year'].astype(int)
# subs_yearly = df.groupby('created_year')['subscribers'].mean()

# plt.figure(figsize=(10, 6))
# subs_yearly.plot(marker='o', color='green')
# plt.xlabel('Year')
# plt.ylabel('Average Subscribers')
# plt.title('Average Subscribers Over the Years')
# plt.grid()
# plt.show()