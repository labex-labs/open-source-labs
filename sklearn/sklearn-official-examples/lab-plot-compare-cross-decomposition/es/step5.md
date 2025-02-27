# CCA (Modo PLS B con deflación simétrica)

Usamos el algoritmo CCA para transformar los datos.

```python
cca = CCA(n_components=2)
cca.fit(X_train, Y_train)
X_train_r, Y_train_r = cca.transform(X_train, Y_train)
X_test_r, Y_test_r = cca.transform(X_test, Y_test)
```
