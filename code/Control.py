#График (точки из файла)
x2=[]
with open('20mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x2.append(float(a))
x4=[]
with open('45mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x4.append(float(a))
x5=[]
with open('50mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x5.append(float(a))
x6=[]
with open('60mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x6.append(float(a))
x7=[]
with open('70mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x7.append(float(a))
x8=[]
with open('80mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x8.append(float(a))
x10=[]
with open('100mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x10.append(float(a))
x12=[]
with open('120mm-c', 'r') as file:
    arr=file.readlines()
    for i in arr:
        a = ''.join(i)
        x12.append(float(a))

#Импорт
from numpy import mean
from math import atan
from matplotlib import pyplot
import matplotlib.pyplot as plt

#Среднее
x=[20, 45, 50, 60, 70, 80, 100, 120]
y=[]
y.append(mean(x2))
y.append(mean(x4))
y.append(mean(x5))
y.append(mean(x6))
y.append(mean(x7))
y.append(mean(x8))
y.append(mean(x10))
y.append(mean(x12))

#Рисование и другое
plt.minorticks_on()
plt.title('Калибровка')
plt.xlabel('Показания датчика (у.е.)')
plt.ylabel('Высота уровня жидкости (мм)')
plt.tick_params(labelsize='medium', width=3)
plt.grid(which='major', linestyle='-.')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
#plt.scatter(x, y, color='k', label='Эксперементальные точки')
plt.errorbar(x, y, 2, fmt='.', linewidth=2, capsize=6, color='k', label='Эксперементальные точки')

#аппроксимация
args=[]
args.append(0.28)
args.append(-29.7)
args.append(25)
args.append(86-18.8)
args.append(0.08)
args.append(-5.4)
args.append(13.2)
with open("data", "w") as outfile:
    outfile.write("\n".join([str(item) for item in args]))
xx=[]
yy=[]
for i in range(50, 130):
    yy.append(i)
    xx.append(args[2] * atan(i*args[0] + args[1]) + args[3] + args[6] * atan(i*args[4] + args[5]))
plt.plot(xx, yy,  color='r', label='аппроксимационная кривая')

plt.legend(fontsize=10)
pyplot.show()