import csv
from os import name #import文と配列
header = ['name','age', 'tel']
yamada = ['山田',25,'08011111111']
sato = ['佐藤', 23,'09022222222']
tanaka = ['田中',30,'07033333333']
kato = ['加藤',10,'08888888']
takahashi = ['高橋',20,'0555555']
ishibashi = ['石橋',30,'0333333']
mylist = [header,yamada,sato,tanaka,kato,takahashi,ishibashi]
for a in mylist:
    print(a)
#csvモジュールを使って1行の内容をCSVファイルに書き込み
with open('test.csv','w',newline="") as f:#第一引数：作るファイル,第二引数：’W’　書く(’ｒ’：読む)＃fという言葉を入れることによって、ｃｓｖファイルが開かれた
    writer = csv.writer(f)#ドットは、～の　csvのwriter関数にｆを入れる　実際のＣＳＶができる
    writer.writerow(header)#開かれた実際のＣＳＶにheaderという配列を書き込む

with open('test2.csv','w',newline="") as f:#csv.writer(f)のwirterow関数にheaderという配列を書き込む　#newline=""中の文字列リセットしてる   : コロン　これの続きですよの意味
    writer = csv.writer(f)
    writer.writerows(mylist)
yamada = ['山田',25,'08011111111']
sato = ['佐藤', 23,'09022222222']
mylist = [yamada,sato]
with open('test2.csv','a',newline="") as f:#csv.writer(f)のwirterow関数にheaderという配列を書き込む　#newline=""中の文字列リセットしてる   : コロン　これの続きですよの意味
    writer = csv.writer(f)
    writer.writerows(mylist)