# Perceptrón

El Perceptrón es un algoritmo de clasificación lineal simple adecuado para el aprendizaje a gran escala. Actualiza su modelo solo en los errores, lo que lo hace más rápido de entrenar que el descenso de gradiente estocástico (SGD) con pérdida de bisagra. Los modelos resultantes también son más esparsos.

Ajustemos un modelo de perceptrón.

```python
clf = linear_model.Perceptron(alpha=0.1)
clf.fit(X, y)

print(clf.coef_)
```

- Creamos una instancia de `Perceptron` con el parámetro de regularización `alpha` establecido en 0.1.
- Utilizamos el método `fit` para ajustar el modelo a los datos de entrenamiento.
- Imprimimos los coeficientes del modelo de perceptrón.
