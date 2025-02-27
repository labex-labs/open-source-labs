# Propagación de Etiquetas

#### Resumen del algoritmo de Propagación de Etiquetas

La Propagación de Etiquetas es un tipo de algoritmo de inferencia semi-supervisada de grafos. Construye un grafo de similitud sobre todos los elementos del conjunto de datos de entrada y utiliza este grafo para propagar las etiquetas de los datos etiquetados a los datos no etiquetados. La Propagación de Etiquetas se puede utilizar para tareas de clasificación y admite métodos de kernel para proyectar los datos a espacios dimensionales alternativos.

#### Uso de la Propagación de Etiquetas en scikit-learn

En scikit-learn, hay dos modelos de propagación de etiquetas disponibles: `LabelPropagation` y `LabelSpreading`. Ambos modelos construyen un grafo de similitud y propagan las etiquetas. Aquí hay un ejemplo de cómo utilizar la Propagación de Etiquetas:

```python
from sklearn.semi_supervised import LabelPropagation

# Crea un modelo de propagación de etiquetas
label_propagation = LabelPropagation()

# Entrena el modelo de propagación de etiquetas en los datos etiquetados
label_propagation.fit(X_labeled, y_labeled)

# Predice las etiquetas para nuevas muestras
y_pred = label_propagation.predict(X_test)
```

En el ejemplo anterior, `X_labeled` e `y_labeled` son los datos etiquetados, y `X_test` son las nuevas muestras a predecir.
