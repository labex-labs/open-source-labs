# Generar el conjunto de Mandelbrot

Ahora generaremos el conjunto de Mandelbrot llamando a la función `mandelbrot_set` con los parámetros deseados. Esto nos dará dos matrices:

- `Z`: los valores finales de los números complejos sobre los que iteramos
- `N`: el número de iteraciones realizadas para cada punto antes de determinar que era parte del conjunto

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
