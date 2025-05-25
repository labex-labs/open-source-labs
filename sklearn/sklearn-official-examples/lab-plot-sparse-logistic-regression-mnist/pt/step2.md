# Carregar o conjunto de dados MNIST

Carregaremos o conjunto de dados MNIST utilizando a função `fetch_openml` do scikit-learn. Também selecionaremos um subconjunto dos dados definindo o número de `train_samples` para 5000.

```python
# Reduzir para uma convergência mais rápida
t0 = time.time()
train_samples = 5000

# Carregar dados de https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
