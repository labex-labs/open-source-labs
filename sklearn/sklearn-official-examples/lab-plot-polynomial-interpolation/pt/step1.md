# Preparar os Dados

Começamos por definir uma função que pretendemos aproximar e preparar o seu gráfico.

```python
def f(x):
    """Função a ser aproximada por interpolação polinomial."""
    return x * np.sin(x)

# Intervalo completo que queremos representar graficamente
x_plot = np.linspace(-1, 11, 100)

# Para tornar mais interessante, apenas fornecemos um pequeno subconjunto de pontos para treino.
x_train = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
x_train = np.sort(rng.choice(x_train, size=20, replace=False))
y_train = f(x_train)

# Criar versões de matrizes 2D destes arrays para alimentar os transformadores
X_train = x_train[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]
```
