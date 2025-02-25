# Определяем функцию для множества Мандельброта

Далее мы определим функцию, которая генерирует множество Мандельброта. Функция принимает несколько параметров:

- `xmin`, `xmax`, `ymin`, `ymax`: минимальные и максимальные значения по осям x и y
- `xn` и `yn`: количество точек, которое нужно сгенерировать вдоль каждой оси
- `maxiter`: максимальное количество итераций, которое нужно выполнить для каждой точки
- `horizon`: максимальное значение, при котором точка считается частью множества

```python
def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn).astype(np.float32)
    Y = np.linspace(ymin, ymax, yn).astype(np.float32)
    C = X + Y[:, None] * 1j
    N = np.zeros_like(C, dtype=int)
    Z = np.zeros_like(C)
    for n in range(maxiter):
        I = abs(Z) < horizon
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z, N
```
