# Définir la fonction de l'ensemble de Mandelbrot

Ensuite, nous allons définir une fonction qui génère l'ensemble de Mandelbrot. La fonction prend plusieurs paramètres :

- `xmin`, `xmax`, `ymin`, `ymax` : les valeurs minimales et maximales pour les axes x et y
- `xn` et `yn` : le nombre de points à générer le long de chaque axe
- `maxiter` : le nombre maximum d'itérations à effectuer pour chaque point
- `horizon` : la valeur maximale à laquelle considérer qu'un point fait partie de l'ensemble

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
