# Создание разрывочной горизонтальной столбчатой диаграммы

На этом шаге мы создадим разрывочную горизонтальную столбчатую диаграмму. Мы будем использовать метод `broken_barh()` класса `Axes` для создания диаграммы. Метод `broken_barh()` принимает три аргумента: первый аргумент - это список кортежей, где каждый кортеж представляет сегмент столбца, а первый элемент кортежа - это точка начала сегмента, а второй элемент - длина сегмента; второй аргумент - это y-координата столбца; и третий аргумент - это цвет заливки столбца.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
