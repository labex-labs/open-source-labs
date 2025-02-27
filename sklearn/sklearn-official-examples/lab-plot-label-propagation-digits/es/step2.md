# Preparar los datos para el aprendizaje semi-supervisado

Seleccionamos 340 muestras y solo 40 de estas muestras están asociadas con una etiqueta conocida. Guardamos los índices de las otras 300 muestras para las cuales no se supone que sepamos sus etiquetas. Luego barajamos las etiquetas de modo que las muestras sin etiquetar estén marcadas con -1.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```
