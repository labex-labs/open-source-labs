# Ajustar o classificador

Após gerar o conjunto de dados, ajustaremos o classificador usando `LogisticRegression` do scikit-learn.

```python
# Ajustar o classificador
clf = LogisticRegression(C=1e5)
clf.fit(X, y)
```
