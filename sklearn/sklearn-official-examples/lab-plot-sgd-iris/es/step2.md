# Entrenar el modelo

Ahora entrenaremos el modelo SGDClassifier en el conjunto de datos iris con la ayuda del método fit(). Este método toma los datos de entrada y los valores objetivo como entrada y entrena el modelo con los datos dados.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
