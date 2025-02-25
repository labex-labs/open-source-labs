# Определить область отображения и создать первое изображение

Определите область отображения и создайте первое изображение с использованием функции `imshow`.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```
