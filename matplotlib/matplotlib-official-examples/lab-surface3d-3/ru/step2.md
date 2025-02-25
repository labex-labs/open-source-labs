# Создаем данные для поверхности

В этом шаге мы создадим данные для поверхности. Мы создадим сетку X и Y, вычислим радиальное расстояние R и вычислим значение Z на основе значения R с использованием `np.sin()`.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
