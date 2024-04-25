from time import sleep
a = int(input('Введите количество секунд '))
sleep(5)
h = a//3600
m = (a-h*3600)//60
s = (a-h*3600-m*60)
print(h, m, s)
