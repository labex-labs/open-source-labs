# Auswählen von Features basierend auf der Wichtigkeit

Wir wählen die zwei am wichtigsten nach den Koeffizienten erscheinenden Features mit `SelectFromModel`. `SelectFromModel` akzeptiert einen `threshold`-Parameter und wird die Features auswählen, deren Wichtigkeit (definiert durch die Koeffizienten) über diesem Schwellenwert liegt.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```
