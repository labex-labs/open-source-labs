# Создаем 3D-график «стеги»

В этом шаге мы создадим 3D-график «стеги» с использованием функции `stem` из Matplotlib. Мы передадим координаты x, y и z в качестве аргументов функции `stem`.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
