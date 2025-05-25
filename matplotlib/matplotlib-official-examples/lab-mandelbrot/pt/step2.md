# Definir a Função do Conjunto de Mandelbrot

Em seguida, definiremos uma função que gera o conjunto de Mandelbrot. A função recebe vários parâmetros:

- `xmin`, `xmax`, `ymin`, `ymax`: os valores mínimo e máximo para os eixos x e y
- `xn` e `yn`: o número de pontos a serem gerados ao longo de cada eixo
- `maxiter`: o número máximo de iterações a serem realizadas para cada ponto
- `horizon`: o valor máximo no qual considerar um ponto como parte do conjunto

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
