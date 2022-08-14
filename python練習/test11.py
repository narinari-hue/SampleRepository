#クラスのメソッドとコンストラクタ
class Car():
# クラスのインスタンス化
    def name(self, name):#今からクラスの名前を入れる作業（関数）をするという宣言する。第１引数＝Car、10行目のベンツ
        self.name = name#設計図の車自身の名前は、引数の名前を入れた。#self.nameというのは、設計図がもつパラメータ
    def run(self):
        print('%s is running' % self.name)#print(self.namae,"is running")でもよい
    def run2(self,car_name):
        print(car_name,"is running")

car = Car()
# nameというインスタンス変数に、値をセットしています
car.name('ベンツ')#第1引数Carが省略されている、第2引数がベンツ
car.run()
# ベンツ is running
# インスタンスは、いくつも作成することができます
car_p = Car()#まず設計図をもとにcar_pを実体化した→→のでnameという機能や走るという機能を使えるようになった
car_p.run()
car_p.name('プリウス')#car-pのname関数を呼び出した。第１引数car-p(それ自身なので省略、第２引数はプリウス)
car_p.run()
car_p.run2('スイフト')