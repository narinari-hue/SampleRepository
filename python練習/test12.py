#コンストラクターその２#test11と12の違いは、インスタンス化するときに、初期値をいれてすぐ動かせるかられるかどうか。

class Car():
    def __init__(self,name, speed, price):#__init__ (最初から動かします)→コンストラクタ　インスタンス化された時に自動的に発動されるメソッド
        self.name = name
        self.speed = speed
        self.price = price#selfは設計図自身という意味。だが、下のマーチということを書いたら、selfはマーチに置き換えられる。（パラメータ、外部から引数をもってくる。）
    def run(self):
        print('%s is running' % self.name)#print(self.name,'is running')でも動く
    @classmethod #@はアノテーション（annotation：注釈）といって、特別な処理を示す#クラスメソッドは一応属しているけど、独立したメソッド
    def create(cls):#clsは、classmethodの略
        print('this is class method')


# クラスのインスタンス化
# インスタンス化した時に、インスタンス変数nameに、値をセットしています。
march = Car("マーチ", 180,65)#マーチを実体化,コンストラクタとしてカッコ内を入れる
print('車名は', march.name,'で、速度は',march.speed,'で、値段は',march.price,'です。') #プロパティは属性なのでカッコいらない。メソッドはカッコいる#プロパティを呼び出している
march.run()#これはメソッドです。#9行目から呼び出している
Car.create()#実体化しないで、（11-12行目から）機能だけ呼び出している
