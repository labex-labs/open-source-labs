# Entrenar el modelo

Ahora entrenaremos el modelo LOF usando los datos de entrenamiento. Establecemos el número de vecinos en 20 y la novedad en verdadera. También establecemos la contaminación en 0.1.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
