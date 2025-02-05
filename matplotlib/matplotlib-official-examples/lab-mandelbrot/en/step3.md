# Generate the Mandelbrot Set

Now we will generate the Mandelbrot set by calling the `mandelbrot_set` function with our desired parameters. This will give us two arrays:

- `Z`: the final values of the complex numbers we iterated over
- `N`: the number of iterations performed for each point before it was determined to be part of the set

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
