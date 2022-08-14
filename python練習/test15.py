import narita_read_data as na
na.konnichiwa()#独立して実行されている。関数なので見えてないが実行している。
print(na.konnichiwa())

na.triangle_area(10,5)#5行目も関数で独立して実行している。関数なので見えてないが実行している。
print(na.triangle_area(100,50))#100*50を計算してから（関数），プリント分として出す

print(na.repeat_addition(2,3))