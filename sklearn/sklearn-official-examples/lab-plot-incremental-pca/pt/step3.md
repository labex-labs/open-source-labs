# Executar IPCA

Vamos executar IPCA ( _Incremental Principal Component Analysis_) no conjunto de dados Iris, inicializando uma instância da classe IPCA e ajustando-a aos dados.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
