# Создание прямоугольной диаграммы "ящик с усами"

Теперь мы создадим прямоугольную диаграмму "ящик с усами" с использованием функции `boxplot()` в Matplotlib. Мы установим параметр `patch_artist` в значение `True`, чтобы заполнить ящик цветом.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # вертикальное выравнивание ящика
                     patch_artist=True,  # заполнение цветом
                     labels=labels)  # метки для оси x
ax1.set_title('Rectangular Box Plot')
```
