# Вычисляем статистику для ящика с усами

Функция `boxplot_stats()` из модуля `matplotlib.cbook` вычисляет статистику, необходимую для построения ящика с усами. Мы передаем в нее данные и метки в качестве параметров.

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
