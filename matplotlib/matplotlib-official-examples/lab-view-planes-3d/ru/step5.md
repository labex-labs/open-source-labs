# Создаем трехмерную диаграмму

Мы используем `subplot_mosaic` для создания трехмерной диаграммы на основе макета, определенного на шаге 4.

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
