# Estimativa de Densidade e Detecção de Novidades

- As máquinas de vetores de suporte (SVMs) também podem ser usadas para estimativa de densidade e detecção de novidades com a classe `OneClassSVM`:

```python
clf = svm.OneClassSVM()
clf.fit(X)
clf.predict(X)
```
