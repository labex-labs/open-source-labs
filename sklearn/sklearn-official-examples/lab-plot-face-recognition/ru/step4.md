# Выполнение метода главных компонент (PCA)

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Мы выполняем метод главных компонент (Principal Component Analysis, PCA) для извлечения признаков из входных данных. Мы устанавливаем количество компонентов равным 150 и обучаем модель PCA на обучающих данных. Затем мы получаем собственные лица (eigenfaces) и преобразуем входные данные в главные компоненты.
