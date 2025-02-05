# Define the Mandelbrot Set Function

Next, we will define a function that generates the Mandelbrot set. The function takes in several parameters:

- `xmin`, `xmax`, `ymin`, `ymax`: the minimum and maximum values for the x and y axes
- `xn` and `yn`: the number of points to generate along each axis
- `maxiter`: the maximum number of iterations to perform for each point
- `horizon`: the maximum value at which to consider a point to be part of the set

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
