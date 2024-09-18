import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


'''
# 1.1.1------------------------------------------------------------------------------------------
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(2 * x)
plt.plot(x, y, color = 'b', linestyle = '-', marker = '', markersize = 3)

plt.title('График функции y = cos(2x)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color = 'black', linewidth = 0.5, ls = '--')  # Добавление горизонтальной линии y=0
plt.axvline(0, color = 'black', linewidth = 0.5, ls = '--')  # Добавление вертикальной линии x=0
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

plt.show()


# 1.1.2------------------------------------------------------------------------------------------
salaries = [21, 19, 27, 11, 102, 25, 21]
employees = ["Коля", "Женя", "Петя", "Саша", "Катя", "Вася", "Жора"]
plt.figure(figsize = (8, 8))
plt.pie(salaries, labels=employees, autopct='%1.1f%%', startangle=140)
plt.title('Распределение зарплат сотрудников', y = 1.05)
plt.axis('equal')

plt.show()


# 1.1.3------------------------------------------------------------------------------------------
x = np.arange(-np.pi, np.pi, 0.1)

y1 = np.sin(2 * x)
y2 = np.sin(x)
fig, axs = plt.subplots(2, 1, figsize=(8, 8))  # 2 строки, 1 столбец

# Построение первого графика
axs[0].plot(x, y1, color='brown', label='sin(2x)')
axs[0].set_title('График функции y = sin(2x)')
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].grid()
axs[0].legend()

# Построение второго графика
axs[1].plot(x, y2, color='blue', label='sin(x)')
axs[1].set_title('График функции y = sin(x)')
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].grid()
axs[1].legend()

plt.tight_layout()
plt.show()


# 1.1.4 - 5-------------------------------------------------------------------------------------
names = ["Коля", "Женя", "Петя", "Саша", "Катя", "Вася", "Жора"]
heights = [21, 19, 27, 11, 102, 25, 21]

plt.bar(names, heights, edgecolor='black')
plt.title("Зарплата сотрудников", y = 1.05, color = "r")
plt.xlabel("Имена сотрудников")
plt.ylabel("Зарплата")

for i, height in enumerate(heights):
    plt.text(i, height + 1, str(height), ha='center', va='bottom')

plt.show()


# 1.1.6------------------------------------------------------------------------------------------
names = ["Коля", "Женя", "Петя", "Саша", "Катя", "Вася", "Жора"]
heights = [21, 19, 27, 11, 102, 25, 21]
plt.hist(heights, bins = range(0, 120, 10), color = 'yellow')

plt.title("Распределение зарплаты")
plt.xlabel("Зарплата")
plt.ylabel("Количество сотрудников")
# округляем ось количества людей до целых
plt.yticks(range(0, max(np.histogram(heights, bins = range(0, 120, 10))[0]) + 1)) 

counts, bins = np.histogram(heights, bins=range(0, 120, 10))
for count, x in zip(counts, bins):
    plt.text(x + 5, count, str(count), ha='center', va='bottom')

plt.xticks(bins)  # Установка меток по оси X
plt.show()


# 1.1.7------------------------------------------------------------------------------------------
x = np.arange(-10, 10, 0.5)          # Значения по оси X
y = np.arange(-10, 10, 0.5)          # Значения по оси Y
x, y = np.meshgrid(x, y)             # Создание сетки
r = np.sqrt(x**2 + y**2)
z = 10 * np.sin(r) / r               # Значения по оси Z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Установка углов просмотра
theta = 30  # Угол поворота вокруг оси Y
phi = 30    # Угол поворота вокруг оси X
ax.view_init(elev = phi, azim = theta)
surf = ax.plot_surface(x, y, z, cmap = 'cool')

# Функция обновления для анимации
def update(frame):
    ax.view_init(elev=30, azim=frame)  # Вращение вокруг оси Z
    return surf,

# Создание анимации
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)

plt.show()


# 1.1.8------------------------------------------------------------------------------------------
x = np.arange(-3, 3, 0.05)
# Создание графического окна и разбивка на 4 части
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Верхнее левое окно: график функции sin(x)
axs[0, 0].plot(x, np.sin(x), color='blue')
axs[0, 0].set_title('График функции sin(x)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('sin(x)')

# Нижнее левое окно: график функции arctg(x)
x = np.arange(-6, 6, 0.05)
axs[1, 0].plot(x, np.arctan(x), color='green')
axs[1, 0].set_title('График функции arctg(x)')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('arctg(x)')

# Нижнее правое окно: график функции e^x
x = np.arange(-2, 1, 0.05)
axs[1, 1].plot(x, np.exp(x), color='red')
axs[1, 1].set_title('График функции e^x')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('e^x')

# Верхнее правое окно: график функции cos(x)
x = np.arange(-3, 3, 0.05)
axs[0, 1].plot(x, np.cos(x), color='purple')
axs[0, 1].set_title('График функции cos(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('cos(x)')
# Настройка общего вида
plt.tight_layout()
plt.show()


# 1.1.9------------------------------------------------------------------------------------------
# 1. Определение значений переменной x
x = np.array([-1, 0, 1, 1.5, 2])

# 2. Определение значений переменной y
y = np.array([0.8, 0.1, 1.05, 2.3, 3.8])

# 3. Вычисление значений функции y = x^2
y_function = x**2

# Создание графического окна
plt.figure(figsize=(10, 6))

# 4. Построение графика экспериментальных данных
plt.scatter(x, y, color = 'red', label = 'Экспериментальные данные', linewidth = 2) # Кружки

# 5. Разрешение построения в графическом окне еще одного графика (в matplotlib это делается автоматически)

# 6. Построение графика функции y = x^2
x_line = np.linspace(-1, 2, 100)
y_line = x_line**2
plt.plot(x_line, y_line, color = 'blue', label = 'y = x^2', linewidth = 2)  # Сплошная линия

# Настройка заголовка и меток
plt.title('График экспериментальных данных и функции y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Горизонтальная линия на уровне y=0
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Вертикальная линия на уровне x=0
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Показ графика
plt.tight_layout()
plt.show()


'''


# 1.1.10-----------------------------------------------------------------------------------------









'''
from ucimlrepo import fetch_ucirepo 
import pandas as pd


iris = fetch_ucirepo(id = 53)  
# data (as pandas dataframes)
df_x = iris.data.features

df_x.plot(x = 'sepal length', y = 'sepal width', marker = 'o', linestyle = '-', color = 'b', title = 'Ирисы Фишера')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.grid()
plt.show()
'''


