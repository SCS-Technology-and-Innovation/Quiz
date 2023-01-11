from sklearn.linear_model import LinearRegression
from random import randint
import pandas as pd

loc = 'https://scs-technology-and-innovation.github.io/casestudy/demo/dataset.csv'
dataset = pd.read_csv(loc) # first line is header

a = 7
c = 5
m = 1097 # ATTENTION: cannot be larger than the dataset size

def select(n = 5, dec = 3):
    chosen = []
    fs = f'{{:.{dec}f}}' # format string
    s = randint(0, m - 1) # random seed
    x = s
    for i in range(n):
        x = (a * x + c) % m
        chosen.append(x)
    subset = dataset.loc[chosen]
    subset.columns = dataset.columns
    X = subset.iloc[:, 0].values.reshape(-1, 1)
    Y = subset.iloc[:, 1].values.reshape(-1, 1)
    model = LinearRegression()  
    model.fit(X, Y)
    ma = model.coef_[0][0]
    mb = model.intercept_[0]
    return (fs.format(ma), fs.format(mb)), s

if __name__ == '__main__':
    print(select()) 
