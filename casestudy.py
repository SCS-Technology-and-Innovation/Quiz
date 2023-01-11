from sklearn.linear_model import LinearRegression
from random import randint
from numpy import array
import pandas as pd

loc = 'https://scs-technology-and-innovation.github.io/casestudy/demo/dataset.csv'
dataset = pd.read_csv(loc) # first row is header

# must match https://github.com/SCS-Technology-and-Innovation/SCS-Technology-and-Innovation.github.io/blob/main/casestudy/demo/select.js
rnga = 7
rngc = 5
rngm = 1097

def select(n = 5, dec = 3):
    chosen = []
    fs = f'{{:.{dec}f}}' # format string
    s = randint(0, rngm - 1) # random seed
    x = s
    use = []
    for i in range(n):
        x = (rnga * x + rngc) % rngm
        use.append(x) # first row is header
    X = []
    Y = []
    use.sort()
    for pos in use:
        row = dataset.iloc[pos]
        X.append(int(row[0]))
        Y.append(row[1])
    model = LinearRegression()  
    model.fit(array(X).reshape(-1, 1), array(Y).reshape(-1, 1))
    ma = model.coef_[0][0]
    mb = model.intercept_[0]
    return (fs.format(ma), fs.format(mb)), s

if __name__ == '__main__':
    print(select()) 
