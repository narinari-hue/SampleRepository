# -*- coding: utf-8 -*-
"""MLtest2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f9OM_sh9YiKhOHV_kEBp4lAo0DnMHeue

# **第2章 サンプルデータを見てみよう**

## 04　scikit-learnのサンプルデータ

### **アヤメのサンプルデータセット**

1.データセットを読み込んでそのまま表示： リスト2.1
"""

from sklearn import datasets
iris = datasets.load_iris()
print(iris)

"""2.特徴量や、分類の名前を確認： リスト2.2


"""

print("特徴量の名前=", iris.feature_names)
print("分類名前=", iris.target_names)
print("分類の値=", iris.target)

"""3.データをデータフレームに入れる: リスト2.3"""

import pandas as pd
df = pd.DataFrame(iris.data)
df.head()

"""4.列名に特徴量を設定して、どんな品種なのかをtargetとして追加: リスト2.4"""

df.columns = iris.feature_names
df["target"] = iris.target
df.head()

"""5.ヒストグラムで描画（3種類の品種を違う色に）: リスト2.5"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

# 3種類の品種を、別々のデータフレームに分ける
# targetの値が0ならdf0に、1ならdf1に、2ならdf2に入れる
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
df2 = df[df["target"]==2]

# 3種類の品種を、ヒストグラムで色分けして描画
# 「がくの幅」で、ヒストグラムを描画
plt.figure(figsize=(5, 5))
xx = "sepal width (cm)"
df0[xx].hist(color="b",alpha=0.5)
df1[xx].hist(color="r",alpha=0.5)
df2[xx].hist(color="g",alpha=0.5)
plt.xlabel(xx)
plt.show()

"""6.散布図で描画（3種類の品種を違う色に）: リスト2.6"""

# 「がくの幅」と「がくの長さ」で、散布図を描画
xx = "sepal width (cm)"
yy = "sepal length (cm)"
plt.figure(figsize=(5, 5))
plt.scatter(df0[xx], df0[yy], color="b", alpha=0.5)
plt.scatter(df1[xx], df1[yy], color="r", alpha=0.5)
plt.scatter(df2[xx], df2[yy], color="g", alpha=0.5)
plt.xlabel(xx)
plt.ylabel(yy)
plt.grid()
plt.show()

"""7.3D散布図で描画（3種類の品種を違う色に）: リスト2.7"""

from mpl_toolkits.mplot3d import Axes3D
# 「がくの幅」と「がくの長さ」と「花びらの長さ」で、3D散布図
xx = "sepal width (cm)"
yy = "sepal length (cm)"
zz = "petal length (cm)"
ax = Axes3D(plt.figure(figsize=(5, 5)))
ax.scatter(df0[xx], df0[yy], df0[zz], color="b")
ax.scatter(df1[xx], df1[yy], df1[zz], color="r")
ax.scatter(df2[xx], df2[yy], df2[zz], color="g")
ax.set_xlabel(xx)
ax.set_ylabel(yy)
ax.set_zlabel(zz)
plt.show()

"""視点を変えると「がくの長さ（赤）」と「花びらの長さ（緑）」の境界線が見える: リスト2.8"""

ax = Axes3D(plt.figure(figsize=(5, 5)))
ax.scatter(df0[xx], df0[yy], df0[zz], color="b")
ax.scatter(df1[xx], df1[yy], df1[zz], color="r")
ax.scatter(df2[xx], df2[yy], df2[zz], color="g")
ax.set_xlabel(xx)
ax.set_ylabel(yy)
ax.set_zlabel(zz)
ax.view_init(0, 240)
plt.show()

"""3D散布図の視点を変えると、2Ｄ散布図と同じ表示に: リスト2.9"""

ax = Axes3D(plt.figure(figsize=(5, 5)))
ax.scatter(df0[xx], df0[yy], df0[zz], color="b")
ax.scatter(df1[xx], df1[yy], df1[zz], color="r")
ax.scatter(df2[xx], df2[yy], df2[zz], color="g")
ax.set_xlabel(xx)
ax.set_ylabel(yy)
ax.set_zlabel(zz)
ax.view_init(90, 270)
plt.show()

"""## 05　サンプルデータセット を自動生成しよう

### **分類データセットの自動生成（塊）**
### **make_blobs**
*   random_state：ランダム生成の種にする番号
*   n_samples：データの個数
*   n_features：特徴量の数
*   centers：塊の数
*   cluster_std：ばらつきの大きさ（標準偏差）

ランダムの種が「3」で、特徴量は2つ、塊数は2つ、ばらつき1の、300個の点でできたデータセット: リスト2.10
"""

from sklearn.datasets import make_blobs
import pandas as pd

X, y = make_blobs(
    random_state=3,
    n_features=2,    
    centers=2,
    cluster_std=1,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
df.head()

"""特徴量0を横軸に、特徴量1を縦軸にして、targetの値で色分けをした散布図を描画: リスト2.11"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt

# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
# 分類0は青、分類1は赤で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.grid()
plt.show()

"""ランダムの種が「3」で、特徴量は2つ、塊数は3つ、ばらつき1の、300個の点でできたデータセット: リスト2.12"""

X, y = make_blobs(
    random_state=3,
    n_features=2,    
    centers=3,
    cluster_std=1,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
df2 = df[df["target"]==2]
# 分類0は青、分類1は赤、分類2は緑で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.scatter(df2[0], df2[1], color="g", alpha=0.5)
plt.grid()
plt.show()

"""ランダムの種が「3」で、特徴量は2つ、塊数は5つ、ばらつき1の、300個の点でできたデータセット: リスト2.13"""

X, y = make_blobs(
    random_state=3,
    n_features=2,    
    centers=5,
    cluster_std=1,
    n_samples=300) 

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
df2 = df[df["target"]==2]
df3 = df[df["target"]==3]
df4 = df[df["target"]==4]
# 分類0は青、1は赤、2は緑、3はマゼンタ、4はシアンで、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.scatter(df2[0], df2[1], color="g", alpha=0.5)
plt.scatter(df3[0], df3[1], color="m", alpha=0.5)
plt.scatter(df4[0], df4[1], color="c", alpha=0.5)
plt.grid()
plt.show()

"""### **分類データセットの自動生成（三日月）**
### **make_moons**
*   random_state：ランダム生成の種にする番号
*   n_samples：データの個数
*   noise：ノイズ

ランダムの種が「3」で、ノイズ0.1、300個の点でできた三日月データセット: リスト2.14
"""

from sklearn.datasets import make_moons
X, y = make_moons(
    random_state=3,
    noise=0.1,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
# 分類0は青、分類1は赤で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.grid()
plt.show()

"""同じ条件で、ノイズ0の三日月データセット: リスト2.15"""

X, y = make_moons(
    random_state=3,
    noise=0,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
# 分類0は青、分類1は赤で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.grid()
plt.show()

"""同じ条件で、ノイズ0.3の三日月データセット: リスト2.16"""

X, y = make_moons(
    random_state=3,
    noise=0.3,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
# 分類0は青、分類1は赤で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.grid()
plt.show()

"""### **分類データセットの自動生成（二重円）**
### **make_circles**
*   random_state：ランダム生成の種にする番号
*   n_samples：データの個数
*   noise：ノイズ

ランダムの種が　「3」で、ノイズ0.1、300個の点でできた二重円のデータセット: リスト2.17
"""

from sklearn.datasets import make_circles
X, y = make_circles(
    random_state=3,
    noise = 0.1,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
# 分類0は青、分類1は赤で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.grid()
plt.show()

"""### **分類データセットの自動生成（同心円）**
### **make_gaussian_quantiles**
*   random_state：ランダム生成の種にする番号
*   n_samples：データの個数
*   n_features：特徴量の数
*   n_classes：グループの数

ランダムの種が「3」で、特徴量は2つ、3つのグループの、300個の点でできた同心円のデータセット: リスト2.18
"""

from sklearn.datasets import make_gaussian_quantiles
X, y = make_gaussian_quantiles(
    random_state=3,
    n_features=2,
    n_classes=3,
    n_samples=300)

# 特徴量（X）でデータフレームを作り、分類（y）をtargetの列として追加
df = pd.DataFrame(X)
df["target"] = y
# 分類によって、別々のデータフレームに分ける
df0 = df[df["target"]==0]
df1 = df[df["target"]==1]
df2 = df[df["target"]==2]
# 分類0は青、分類1は赤、分類2は緑で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df0[0], df0[1], color="b", alpha=0.5)
plt.scatter(df1[0], df1[1], color="r", alpha=0.5)
plt.scatter(df2[0], df2[1], color="g", alpha=0.5)
plt.grid()
plt.show()

"""### **回帰データセットの自動生成**
### **make_gaussian_quantiles**
*   random_state：ランダム生成の種にする番号
*   n_samples：データの個数
*   n_features：特徴量の数
*   noise：ノイズ
*   bias：y切片

ランダムの種が「3」で、特徴量は1つ、ノイズ10、Xが0のとき100を通る線の、300個の点でできたデータセット: リスト2.19
"""

from sklearn.datasets import make_regression
X, y = make_regression(
    random_state=3,
    n_features=1,
    noise=10,
    bias = 100, 
    n_samples=300)

# データフレームを作り
df = pd.DataFrame(X)
# 「特徴量0」と「y」で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df[0], y, color="b", alpha=0.5)
plt.grid()
plt.show()

"""同じ条件で、ノイズ0のデータセット: リスト2.20"""

from sklearn.datasets import make_regression
X, y = make_regression(
    random_state=3,
    n_features=1,
    noise=0,
    bias = 100,
    n_samples=300)

# データフレームを作り
df = pd.DataFrame(X)
# 「特徴量0」と「y」で、散布図を描画
plt.figure(figsize=(5, 5))
plt.scatter(df[0], y, color="b", alpha=0.5)
plt.grid()
plt.show()