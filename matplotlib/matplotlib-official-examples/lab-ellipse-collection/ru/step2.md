# Создаем данные для эллипсов

Создаем данные для наших эллипсов в виде массивов координат x, координат y, ширины, высоты и угла.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
