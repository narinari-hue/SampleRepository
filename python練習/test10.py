#抽象的で、良いクラス名
class Car:#クラス宣言　大文字からはいる
    def run(self):#def:define=>メソッドの定義#run(self): selfはCar自身を示しており、Car自身がprintしてる

        print('car run')#1～5が設計図
        price = 2000000
        print(price)
    
#クラスのインスタンス化
car = Car()#Car()は関数であり設計図
#インスタンス化すると、メソッドを使えます。
car.run()#ドット（～の）
#car run
march = Car()
march.run()
