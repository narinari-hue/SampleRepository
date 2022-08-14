import pandas as pd #pandasのインポート 
import matplotlib.pyplot as plt # グラフ描画用
import numpy as np # 基本ライブラリ
import csv
import seaborn as sns #12-06ヒートマップ用


df = pd.read_csv('hutatsune.csv')#12-6 ローカル用に設定
df2 = df

#相関ヒートマップ関連
xcol_2 =['H_temp','L_temp','daylight_hours(h)','water_temperature','salt','wind_speed','Density','sigma_t','DO','Chl-a']
df3 = df2[xcol_2]

corr = df3.corr()
print(corr)