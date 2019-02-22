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
    plt.clf()
    #plt.ylim((0, 1e14))
    plt.bar(index,num_movies)
    plt.xlabel('Country Name',fontsize = 5)
    plt.ylabel('GDP',fontsize = 5)
    plt.xticks(index,label,fontsize =5, rotation = 30)
    plt.title('GDP for Countries in ' + Year)
    plt.pause(0.5)
    fig1.canvas.draw()
    #plt.show()

def Data_select(Data, Year, Country_List):
    Data = Data.sort_values(Year,ascending=False)
    Data  = Data.loc[Country_List]
    #Data = Data.head(n=num_countries)
    label = Data['Country Name']
    num_movies = Data[Year]
    return label, num_movies


Data = read_data()
Data.index = Data['Country Name']
Country_List = ["United States", "United Kingdom", "France", "China", "Japan", "Canada","Italy", "India","Australia","Brazil"]
Years = list(Data)[4:-2]
print(Years)
for i in range(len(Years)):
    num_of_countries = 1
    label, num_movies = Data_select(Data, Years[i],Country_List)
    plot_bar(label,num_movies,Years[i])
