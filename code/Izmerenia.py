#График (точки из файла)
args=[]
with open('data', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        args.append(float(a))
y2=[]
with open('20mm-i', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        y2.append(float(a))
y4=[]
with open('45mm-i', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        y4.append(float(a))
y8=[]
with open('80mm-i', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        y8.append(float(a))
y12=[]
with open('120mm-i', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        y12.append(float(a))

#Время
x2=[]
tay = 20 / len(y2)
for i in range(len(y2)):
    x2.append(i*tay)
x4=[]
tay = 20 / len(y4)
for i in range(len(y4)):
    x4.append(i*tay)
x8=[]
tay = 20 / len(y8)
for i in range(len(y8)):
    x8.append(i*tay)
x12=[]
tay = 20 / len(y12)
for i in range(len(y12)):
    x12.append(i*tay)

#Калибровка
from math import atan
c2=[]
for i in range(len(y2)):
    c2.append(args[2] * atan(y2[i]*args[0] + args[1]) + args[3] + args[6] * atan(y2[i]*args[4] + args[5]))
c4=[]
for i in range(len(y4)):
    c4.append(args[2] * atan(y4[i]*args[0] + args[1]) + args[3] + args[6] * atan(y4[i]*args[4] + args[5]))
c8=[]
for i in range(len(y8)):
    c8.append(args[2] * atan(y8[i]*args[0] + args[1]) + args[3] + args[6] * atan(y8[i]*args[4] + args[5]))
c12=[]
for i in range(len(y12)):
    c12.append(args[2] * atan(y12[i]*args[0] + args[1]) + args[3] + args[6] * atan(y12[i]*args[4] + args[5]))
#Импорт
from matplotlib import pyplot
import matplotlib.pyplot as plt

#Рисование крестов и другое
plt.minorticks_on()
plt.title('Определение τ при 45мм')
plt.xlabel('Время измерения (с)')
plt.ylabel('Высота уровня жидкости (мм)')
plt.tick_params(labelsize='medium', width=3)
plt.grid(which='major', linestyle='-.')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.text(2, 25,'Значение τ: 1.81 секунд')
plt.xlim([0, 4])
#plt.scatter(x2, y2, color='k', label='Эксперементальные точки')
#plt.errorbar(x2, y2, 2, fmt='.', linewidth=2, capsize=6, color='k', label='Эксперементальные точки')
#plt.plot(x2, c2,  color='b', label='При 20мм')
plt.plot(x8, c8,  color='g', label='Эксперементальная зависимость')
#plt.plot(x8, c8,  color='g', label='При 80мм')
#plt.plot(x12, c12,  color='y', label='При 120мм')

#Апроксимация
xx=[]
yy=[]
for i in range(3):
    xx.append(i)
    yy.append(100)
plt.plot(xx, yy, color='r', label='Аппроксимационная прямая')
xxx=[]
yyy=[]
for i in range(3, 7):
    xxx.append(i/2)
    yyy.append(-54*i/2 + 198)
plt.plot(xxx, yyy, color='r')
print("Значение a:", a)


plt.legend(fontsize=10)
pyplot.show()