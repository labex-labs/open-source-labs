# Заполнение диаграмм "ящик с усами" пользовательскими цветами

Далее мы заполним диаграммы "ящик с усами" пользовательскими цветами. Мы создадим список цветов и используем цикл, чтобы заполнить каждый ящик разным цветом.

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
