import pandas as pd # 一般的にpandasはpdと名前を付けてimportされる
#まず2つのCSVを読み込む
df=pd.read_csv('student.csv')
df2=pd.read_csv('universities.csv')
#dfは学校IDをキーに，df2はIDをキーに内部結合
df_merged=pd.merge(df,df2,left_on='学校ID',right_on='ID')
#print(df_merged)
#how='left'を指定#左外部結合#左外部結合したやつをｃｓｖで保存
df_merged=pd.merge(df,df2,left_on='学校ID',right_on='ID',how='left')
#print(df_merged)
#print(df.iloc[:, :])
#print(df.iloc[:3, :2])
#print(df.iloc[1:3, 1:2])#1行以上、3行未満#1列以上、2列未満
df3=df2.iloc[2:10, 1:4]
print(df3)