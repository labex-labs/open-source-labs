# Realizar Análisis de Componentes Principales (PCA)

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Realizamos el Análisis de Componentes Principales (PCA) para extraer características de los datos de entrada. Establecemos el número de componentes en 150 y ajustamos el modelo PCA a los datos de entrenamiento. Luego obtenemos las eigenfaces y transformamos los datos de entrada en componentes principales.
