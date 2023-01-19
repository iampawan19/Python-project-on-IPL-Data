# -*- coding: utf-8 -*-
"""IPL Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hp2l5iWY0WTuYogWhSltfQtiD_ZHTj_l
"""

import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns

from google.colab import files

uploaded = files.upload()

uploaded

ipl=pd.read_csv('Match.csv')

#having first five records
ipl.head()

#looking at the number of rows and columns in dataset
ipl.shape

#Getting freq. of most man of the Match
ipl['ManOfMach'].value_counts()

#Getting top 10 player man of the match
ipl['ManOfMach'].value_counts()[0:10]

#Getting top 5 player man of the match
ipl['ManOfMach'].value_counts()[0:5]

#List of the top Man of the match player
list(ipl['ManOfMach'].value_counts()[0:10].keys())

#Bar-Graph of the players
plt.figure(figsize=(15,6))
plt.bar(list(ipl['ManOfMach'].value_counts()[0:10].keys()),list(ipl['ManOfMach'].value_counts()[0:10]),color='b')
plt.show()

#Find the Number of toss wins w.r.t each team
ipl['Toss_Winner'].value_counts()

#Toss ratio
ipl['Toss_Name'].value_counts()

#Getting wins Margin
ipl['Win_Margin'].value_counts

#Making a histogram of winning margin
plt.figure(figsize=(5,7))
plt.hist(ipl['Win_Margin'])
plt.title("Winning Margin")
plt.xlabel("Runs")
plt.show()

#Extracting the records where team won by first batting
batting_first=ipl[ipl['Win_Type']=='runs']

batting_first.head()

#Making a histogram of the first batting team
plt.figure(figsize=(5,7))
plt.hist(batting_first['Win_Type'])
plt.title("Distribution of runs")
plt.xlabel("Runs")
plt.show()

#Finding out the number of wins w.r.t each team after batting first
batting_first['match_winner'].value_counts()

#Making a bar-plot for top 3 team with the most wins after batting first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['match_winner'].value_counts()[0:3].keys()),list(batting_first['match_winner'].value_counts()[0:3]),color=["y","b",'purple'])
plt.show()

#Making a pie-chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['match_winner'].value_counts()),labels=list(batting_first['match_winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

#Extracting those records where a team has won after batting second
batting_second=ipl[ipl['Win_Type']=='wickets']

#looking first five records
batting_second.head()

##Finding out the number of wins w.r.t each team after batting second
batting_second['match_winner'].value_counts()

#Making Bar-chart to find the top 3 team won most after batting second
plt.figure(figsize=(6,6))
plt.bar(list(batting_second['match_winner'].value_counts()[0:3].keys()),list(batting_second['match_winner'].value_counts()[0:3]),color=["purple","b",'red'])
plt.show()

#Making Pie-chart for most wins after batting second 
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['match_winner'].value_counts()),labels=list(batting_second['match_winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()

#looking at match played in each season
 ipl['Season_Year'].value_counts()

#Looking at match played in each city
ipl['Venue_Name'].value_counts()

#Bar graph of most played matches in city
plt.figure(figsize=(6,6))
plt.bar(list(ipl['Venue_Name'].value_counts()[0:3].keys()),list(ipl['Venue_Name'].value_counts()[0:3]),color=["r","b",'g'])
plt.show()

#finding out how many a team won the match after winning the toss
import numpy as np
np.sum(ipl['Toss_Winner']==ipl['match_winner'])

