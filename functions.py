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