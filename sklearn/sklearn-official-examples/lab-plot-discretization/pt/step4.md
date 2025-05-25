# Discretizar a Característica de Entrada

Neste passo, usaremos a classe `KBinsDiscretizer` para discretizar a característica de entrada. Criaremos 10 bins e usaremos a codificação one-hot para transformar os dados.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
