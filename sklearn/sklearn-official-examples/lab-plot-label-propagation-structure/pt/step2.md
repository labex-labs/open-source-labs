# Gerar Conjunto de Dados

Em seguida, geramos um conjunto de dados contendo dois círculos concêntricos usando `make_circles`. Atribuímos etiquetas ao conjunto de dados de forma que todas as amostras sejam desconhecidas, exceto duas amostras, que pertencem aos círculos externo e interno, respectivamente.

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
