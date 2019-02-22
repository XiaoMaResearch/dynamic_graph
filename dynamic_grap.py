import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
def read_data():
    filename = "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10475113/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10475113.csv"
    Data = pd.read_csv(filename,skiprows=4)
    return Data
def plot_bar(label, num_movies):
    index = np.arange(len(label))
    plt.bar(index,num_movies)
    plt.xlabel('Country Name',fontsize = 5)
    plt.ylabel('GDP',fontsize = 5)
    plt.xticks(index,label,fontsize =5, rotation = 30)
    plt.title('GDP for Countries in 2016')
    plt.show()
    
Data = read_data();
Data = Data.sort_values('2016',ascending=False)
Data = Data.head(n=40)
label = Data['Country Name']
print(type(label))
num_movies = Data['2016']
print(type(num_movies))
print(Data.shape)
print(label.shape)
print(num_movies.shape)
plot_bar(label, num_movies)
