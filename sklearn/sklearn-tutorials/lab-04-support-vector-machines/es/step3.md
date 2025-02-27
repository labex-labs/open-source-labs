# Puntuaciones y Probabilidades

- Las SVM no proporcionan directamente estimaciones de probabilidad, pero puede habilitar la estimación de probabilidad estableciendo el parámetro `probability` en `True`:

```python
clf = svm.SVC(probability=True)
clf.fit(X, y)
```

- Luego puede utilizar el método `predict_proba` para obtener las probabilidades de cada clase:

```python
clf.predict_proba([[2., 2.]])
```

- Tenga en cuenta que la estimación de probabilidad es costosa y requiere validación cruzada, por lo que úsela con prudencia.
