import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('hutatsune.csv')

#train_x = df[['sigma_t']]
train_x = df.drop(['Chl-a','date'], axis=1)#説明変数(dropが除く、axis=1が列 axis=0が行)
train_y = df['Chl-a']#目的変数
(train_x, test_x ,train_y, test_y) = train_test_split(train_x, train_y, test_size = 0.3)#テストをする。意味
print(train_x)
clf = RandomForestRegressor(max_depth=4, n_estimators=50, random_state=0)
clf.fit(train_x, train_y)

y_pred = clf.predict(test_x)
accuracy = r2_score(test_y, y_pred)
print('Accuracy: {}'.format(accuracy))
