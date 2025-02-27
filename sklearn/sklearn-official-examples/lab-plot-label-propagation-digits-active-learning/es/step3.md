# Entrenar el modelo de propagación de etiquetas

Ahora entrenaremos un modelo de propagación de etiquetas con los puntos de datos etiquetados y lo utilizaremos para predecir las etiquetas de los puntos de datos no etiquetados restantes.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
