import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
def read_data():
    filename = "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10475113/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_10475113.csv"
    Data = pd.read_csv(filename,skiprows=4)
    return Data
def plot_bar(label, num_movies, Year):
    color_list =['r','g','b','c','m','y','k','Olive','burlywood','chartreuse']
    index = np.arange(len(label))
    fig1 = plt.figure(1)
    plt.clf()
    barlist = plt.barh(index,num_movies/1e9,color =color_list)
    plt.ylabel('Country Name',fontsize = 5)
    plt.xlabel('GDP',fontsize = 5)
    plt.yticks(index,label,fontsize =5, rotation = 0)
    plt.title('Wolrd GDP by Country  in Billions USD ' + 'Year ' + Year  )
    plt.pause(0.5)
    plt.grid(True)
    fig1.canvas.draw()

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
for i in range(len(Years)):
    label, num_movies = Data_select(Data, Years[i],Country_List)
    plot_bar(label,num_movies,Years[i])
