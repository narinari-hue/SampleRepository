import test13b as t13

ito = t13.Person(20,"学生",70,1.6,"女性")#ctrl+F 置換



print('私は', ito.age,'で、', ito.profession,'で、体重は', ito.weight,'kgで、身長は', ito.height,'cmで、性別は', ito.gender, 'です。')

print('私は', ito.bmi_calculation(),'です。')#ito.bmi()ではダメ、クラスのメッソドito.bmi_calculation()と記載する。
