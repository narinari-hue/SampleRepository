# ライブラリのimport
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#csvファイルの読み込み
df = pd.read_csv('hutatsune.csv',encoding='shift-jis')
# データフレームを1日毎のデータにリサンプリングする

# ヒートマップの作成
sns.heatmap(df, annot=True)
df_corr = df.corr()

print(df_corr)
sns.heatmap(df_corr)
