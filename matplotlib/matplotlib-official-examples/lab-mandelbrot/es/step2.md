# Definir la función del conjunto de Mandelbrot

A continuación, definiremos una función que genera el conjunto de Mandelbrot. La función toma varios parámetros:

- `xmin`, `xmax`, `ymin`, `ymax`: los valores mínimo y máximo para los ejes x e y
- `xn` e `yn`: el número de puntos a generar a lo largo de cada eje
- `maxiter`: el número máximo de iteraciones a realizar para cada punto
- `horizon`: el valor máximo en el que se considera que un punto es parte del conjunto

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
