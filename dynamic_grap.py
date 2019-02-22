import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
def read_data():
    filename = "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10475113/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10475113.csv"
    Data = pd.read_csv(filename,skiprows=4)
    return Data
def plot_bar(label, num_movies, Year):
    index = np.arange(len(label))
    fig1 = plt.figure(1)
    plt.ylim((0, 1e14))
    plt.bar(index,num_movies)
    plt.xlabel('Country Name',fontsize = 5)
    plt.ylabel('GDP',fontsize = 5)
    plt.xticks(index,label,fontsize =5, rotation = 30)
    plt.title('GDP for Countries in ' + Year)
    plt.pause(3.0)
    fig1.canvas.draw()
    #plt.show()

def Data_select(Data, Year, num_countries):
    Data = Data.sort_values(Year,ascending=False)
    Data = Data.head(n=num_countries)
    label = Data['Country Name']
    num_movies = Data[Year]
    return label, num_movies

Years = ['1970','1990','2010']

for i in range(len(Years)):
    Data = read_data()
    num_of_countries = 1
    label, num_movies = Data_select(Data, Years[i],num_of_countries)
    plot_bar(label,num_movies,Years[i])
