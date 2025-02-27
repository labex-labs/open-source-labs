# Effectuer l'IPCA

Nous allons effectuer l'IPCA sur l'ensemble de données Iris en initialisant une instance de la classe IPCA et en l'ajustant aux données.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
