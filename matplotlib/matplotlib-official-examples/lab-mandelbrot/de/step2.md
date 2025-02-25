# Definieren der Mandelbrot-Menge-Funktion

Als nächstes definieren wir eine Funktion, die die Mandelbrot-Menge generiert. Die Funktion nimmt mehrere Parameter entgegen:

- `xmin`, `xmax`, `ymin`, `ymax`: die minimalen und maximalen Werte für die x- und y-Achsen
- `xn` und `yn`: die Anzahl der Punkte, die entlang jeder Achse generiert werden sollen
- `maxiter`: die maximale Anzahl an Iterationen, die für jeden Punkt durchgeführt werden sollen
- `horizon`: der maximale Wert, ab dem ein Punkt als Teil der Menge betrachtet wird

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
