# Executar PCA

Vamos executar PCA (Análise de Componentes Principais) no conjunto de dados Iris, inicializando uma instância da classe PCA e ajustando-a aos dados.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
