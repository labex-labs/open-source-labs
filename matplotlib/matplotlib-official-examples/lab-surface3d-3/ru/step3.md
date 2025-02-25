# Создаем цвета для поверхности

В этом шаге мы создадим цвета для поверхности. Мы создадим пустой массив строк с той же формой, что и сетка, и заполним его двумя цветами в чехловом узоре.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
