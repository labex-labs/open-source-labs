# Preparação dos Dados

Vamos gerar alguns dados sintéticos para classificação. A função a ser classificada é definida como:

```python
def g(x):
    """A função a prever (a classificação consistirá então em prever
    se g(x) <= 0 ou não)"""
    return 5.0 - x[:, 1] - 0.5 * x[:, 0] ** 2.0
```

Em seguida, precisamos criar o desenho do experimento e as observações.

```python
# Algumas constantes
lim = 8

# Desenho do experimento
X = np.array(
    [
        [-4.61611719, -6.00099547],
        [4.10469096, 5.32782448],
        [0.00000000, -0.50000000],
        [-6.17289014, -4.6984743],
        [1.3109306, -6.93271427],
        [-5.03823144, 3.10584743],
        [-2.87600388, 6.74310541],
        [5.21301203, 4.26386883],
    ]
)

# Observações
y = np.array(g(X) > 0, dtype=int)
```
