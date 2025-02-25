# Создание диаграммы "ящик с усами" с зазором

Теперь мы создадим диаграмму "ящик с усами" с зазором с использованием функции `boxplot()`. Мы установим параметр `notch` в значение `True`, чтобы создать диаграмму "ящик с усами" с зазором.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # форма зазора
                     vert=True,  # вертикальное выравнивание ящика
                     patch_artist=True,  # заполнение цветом
                     labels=labels)  # метки для оси x
ax2.set_title('Notched Box Plot')
```
