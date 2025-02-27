# Descenso de Gradiente Estocástico (SGD)

El Descenso de Gradiente Estocástico (SGD) es un enfoque simple pero eficiente para el entrenamiento de modelos lineales. Es particularmente útil cuando el número de muestras y características es muy grande. El SGD actualiza los parámetros del modelo utilizando un subconjunto pequeño de los datos de entrenamiento en cada iteración, lo que lo hace adecuado para el aprendizaje en línea y el aprendizaje fuera de núcleo.

Ajustemos un modelo de regresión logística utilizando SGD.

```python
clf = linear_model.SGDClassifier(loss="log_loss", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- Creamos una instancia de `SGDClassifier` con el parámetro `loss` establecido en "log_loss" para realizar la regresión logística.
- Utilizamos el método `fit` para ajustar el modelo a los datos de entrenamiento.
- Imprimimos los coeficientes del modelo de regresión logística obtenido utilizando SGD.
