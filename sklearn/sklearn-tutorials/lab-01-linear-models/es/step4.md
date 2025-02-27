# Regresión Logística

La regresión logística es un método de clasificación que estima las probabilidades de los posibles resultados utilizando una función logística. Se utiliza comúnmente para tareas de clasificación binaria. La regresión logística también se puede extender para manejar problemas de clasificación multi-clase.

Ajustemos un modelo de regresión logística.

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- Creamos una instancia de `LogisticRegression` con el parámetro `random_state` establecido en 0.
- Utilizamos el método `fit` para ajustar el modelo a los datos de entrenamiento.
- Imprimimos los coeficientes del modelo de regresión logística.
