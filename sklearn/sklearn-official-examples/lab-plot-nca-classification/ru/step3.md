# Создание цветовых карты

Теперь мы создадим цветовые карты для построения границ решения классов. Для фона мы будем использовать светлые цвета, а для цветов классов - яркие.

```python
h = 0.05  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF"])
cmap_bold = ListedColormap(["#FF0000", "#00FF00", "#0000FF"])
```
