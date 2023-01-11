from sklearn.linear_model import LinearRegression
import pandas as pd

from sys import argv

loc = argv[1]
dataset = pd.read_csv(loc) # first line is header
X = dataset.iloc[:, 0].values.reshape(-1, 1)
Y = dataset.iloc[:, 1].values.reshape(-1, 1)
model = LinearRegression()  
model.fit(X, Y)
ma = model.coef_[0][0]
mb = model.intercept_[0]
print(ma, mb)
