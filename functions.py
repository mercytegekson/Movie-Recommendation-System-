import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


def readable_date(column, df):
    df["timestamp_x"] = pd.to_datetime(df["timestamp_x"])
    df["timestamp_y"] = pd.to_datetime(df["timestamp_y"])
    #using dt.strftime() method since it is pandas timestamp format
    df["rating_timestamp"] = df["timestamp_x"].dt.strftime("%Y-%m-%d %H:%M:%S")
    df["tag_timestamp"] = df["timestamp_y"].dt.strftime("%Y-%m-%d %H:%M:%S")
    return df.drop(columns=["timestamp_x", "timestamp_y"], axis= 1).head()

### EDA
#writting helper function to help us make x-axis countplots in our EDA process
def sns_xcount(column , data):
    sns.countplot(x = column, data = data, hue= column)
    plt.title(f"{column} count in our data set")
    plt.show();

#writting helper function to help us make y-axis countplots in our EDA process
def sns_ycount(column , data):
    sns.countplot(y = column, data = data)
    plt.title(f"{column} count in our data set")
    plt.show();