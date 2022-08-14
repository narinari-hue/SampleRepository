#宿題（自己紹介の作成）

class Person:
    def __init__(self,self.name, self.profession, self.weight,self.tall,self.gender,self.bmi)
    self.name = '佐藤'
    self.profession = "先生"
    self.weight = 60
    self.tall = 170
    self.gender = "男性"
    self.bmi = weight/(tall*tall)#BMI ＝ 体重kg ÷ (身長m)2
    def introduce(self, profession, weight, tall, gender, bmi):
        print('{}は{}で{}kg{}cm{}です。'.format(self.name, profession, weight, tall, gender, bmi)

#bmi開始
h = Person('佐藤',60,170,'男性',3)
print('{}は{}で{}kg{}cm{}です。'.format(h.name, h.profession, h.body_weight, h.height, h.gender,h.bmi)