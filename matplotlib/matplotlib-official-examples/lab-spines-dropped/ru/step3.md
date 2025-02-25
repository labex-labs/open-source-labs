# Создание фигуры и осей

Мы создадим фигуру и объект оси с использованием `plt.subplots()`. Функция `imshow()` используется для отображения случайных данных в виде изображения.

```python
fig, ax = plt.subplots()

image = np.random.uniform(size=(10, 10))
ax.imshow(image, cmap=plt.cm.gray)
ax.set_title('dropped spines')
```
