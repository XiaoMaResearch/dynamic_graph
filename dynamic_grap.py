import matplotlib.pyplot as plt
import numpy as np
label = ['Adventure', 'Action', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical',
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', 'Multiple Genres', 'Reality']

num_movies = [
    941,
    854,
    4595,
    2125,
    942,
    509,
    548,
    149,
    1952,
    161,
    64,
    61,
    35,
    5
]

def plot_bar():
    index = np.arange(len(label))
    plt.bar(index,num_movies)
    plt.xlabel('Genre',fontsize = 5)
    plt.ylabel('Num of Movies',fontsize = 5)
    plt.xticks(index,label,fontsize =5, rotation = 30)
    plt.title('Market Share for Each Genre 1995-2017')
    plt.show()


plot_bar()
