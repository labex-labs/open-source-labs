# Realizar IPCA

Realizaremos el IPCA en el conjunto de datos Iris inicializando una instancia de la clase IPCA y ajustándola a los datos.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
