# Ajustar OneClassSVM

Neste passo, ajustaremos o modelo OneClassSVM aos dados de treino. Padronizaremos as características e ajustaremos o modelo OneClassSVM aos dados de treino.

```python
# Padronizar características
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# Ajustar OneClassSVM
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.5)
clf.fit(train_cover_std)
```
