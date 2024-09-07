import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import pandas as pd



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
'''






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


