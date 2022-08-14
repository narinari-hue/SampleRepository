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
xtics=["最高気温",'最低気温','日照時間','水温','塩分','風力','密度','sigma_t','DO','Chl-a']
ytics=["最高気温",'最低気温','日照時間','水温','塩分','風力','密度','sigma_t','DO','Chl-a']
ig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(data=corr, cmap="RdBu_r", annot=True, vmax=1, vmin=-1, linecolor="white", linewidths=.5, square=True,xticklabels=xtics,yticklabels=ytics)

sns.pairplot(df3)
