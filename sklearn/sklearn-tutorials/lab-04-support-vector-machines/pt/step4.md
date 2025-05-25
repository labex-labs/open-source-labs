# Problemas Desbalanceados

- As máquinas de vetores de suporte (SVMs) podem lidar com problemas desbalanceados ajustando o parâmetro `class_weight`:

```python
clf = svm.SVC(class_weight={1: 10})
clf.fit(X, y)
```
