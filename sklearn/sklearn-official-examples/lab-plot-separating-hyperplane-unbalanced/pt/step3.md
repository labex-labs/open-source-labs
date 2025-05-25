# Ajustar o Modelo

Ajustaremos o modelo e obteremos o hiperplano separador usando a função `SVC` da biblioteca `svm`. Usaremos um kernel linear e definiremos `C` como 1.0.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
