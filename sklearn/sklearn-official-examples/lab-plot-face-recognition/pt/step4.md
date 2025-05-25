# Executar PCA

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Realizamos a Análise de Componentes Principais (PCA) para extrair características dos dados de entrada. Definimos o número de componentes para 150 e ajustamos o modelo PCA aos dados de treinamento. Em seguida, obtemos as faces próprias e transformamos os dados de entrada em componentes principais.
