# Ajustar OneClassSVM

En este paso, ajustaremos el modelo OneClassSVM a los datos de entrenamiento. Estándarizaremos las características y ajustaremos el modelo OneClassSVM a los datos de entrenamiento.

```python
# Estándarizar características
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# Ajustar OneClassSVM
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.5)
clf.fit(train_cover_std)
```
