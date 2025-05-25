# Pontuações e Probabilidades

- As máquinas de vetores de suporte (SVMs) não fornecem diretamente estimativas de probabilidade, mas você pode habilitar a estimativa de probabilidade definindo o parâmetro `probability` como `True`:

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- Em seguida, você pode usar o método `predict_proba` para obter as probabilidades de cada classe:

```python
clf.predict_proba([[2., 2.]])
```

- Observe que a estimativa de probabilidade é cara e requer validação cruzada, portanto, utilize-a criteriosamente.
