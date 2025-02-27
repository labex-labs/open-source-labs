# Ajuster OneClassSVM

Dans cette étape, nous allons ajuster le modèle OneClassSVM aux données d'entraînement. Nous allons standardiser les caractéristiques et ajuster le modèle OneClassSVM aux données d'entraînement.

```python
# Standardiser les caractéristiques
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# Ajuster OneClassSVM
clf = svm.OneClassSVM(nu=0.1, noyau="rbf", gamma=0.5)
clf.fit(train_cover_std)
```
