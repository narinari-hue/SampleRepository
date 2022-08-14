import pandas as pd # 一般的にpandasはpdと名前を付けてimportされる
#まず2つのCSVを読み込む
df=pd.read_csv('student.csv')
df2=pd.read_csv('universities.csv')
#dfは学校IDをキーに，df2はIDをキーに内部結合
df_merged=pd.merge(df,df2,left_on='学校ID',right_on='ID')

print(df_merged)