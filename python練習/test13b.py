class Person():
    def __init__(self, age, profession, weight, height, gender):
        self.age = age
        self.profession = profession
        self.weight = weight
        self.height = height
        self.gender = gender#selfは、イニット関数だけ（コンストラクターだけ）。
    def bmi_calculation(self):#佐藤自身が入って、佐藤自身が動かすため、最初にself入れる#メソッドbmi_calculation
        bmi = (self.weight / (self.height*self.height))
        return float (bmi)#float型（小数点込み）#int型（整数にする）
        
#sato = Person(30,"先生",60,1.7,"男性")
#print('私は', sato.age,'で、', sato.profession,'で、体重は', sato.weight,'kgで、身長は', sato.height,'cmで、性別は', sato.gender, 'です。')

#print('私は', sato.bmi_calculation(),'です。')#sato.bmi()ではダメ、クラスのメッソドsato.bmi_calculation()と記載する。