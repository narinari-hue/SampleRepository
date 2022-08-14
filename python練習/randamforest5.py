import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score


df = pd.read_csv('hutatsune.csv')

#train_x = df[['sigma_t']]
train_x = df.drop(['Chl-a','date'], axis=1)#説明変数(dropが除く、axis=1が列 axis=0が行)
train_y = df['Chl-a']#目的変数
(train_x, test_x ,train_y, test_y) = train_test_split(train_x, train_y, test_size = 0.3)#テストをする。意味
#条件設定
max_score = 0
SearchMethod = 0
RFC_grid = {RandomForestRegressor(): {"n_estimators": [i for i in range(1, 21)],
                                       
                                       "max_depth":[i for i in range(1, 5)],
                                       "random_state": [i for i in range(0, 101)]
                                      }}

#ランダムフォレストの実行
for model, param in tqdm(RFC_grid.items()):
    clf = GridSearchCV(model, param)
    clf.fit(train_x, train_y)
    pred_y = clf.predict(test_x)
    score = f1_score(test_y, pred_y, average="micro")

    if max_score < score:
        max_score = score
        best_param = clf.best_params_
        best_model = model.__class__.__name__

print("ベストスコア:{}".format(max_score))
print("モデル:{}".format(best_model))
print("パラメーター:{}".format(best_param))

#ハイパーパラメータを調整しない場合との比較
model = RandomForestRegressor()
model.fit(train_x, train_y)
score = model.score(test_x, test_y)
print("")
print("デフォルトスコア:", score)


