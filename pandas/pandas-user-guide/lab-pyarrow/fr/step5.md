# Opérations avec PyArrow

L'intégration des structures de données PyArrow est implémentée via l'interface ExtensionArray de pandas. La fonctionnalité prise en charge existe là où cette interface est intégrée dans l'API pandas.

```python
# Créez une série pandas avec un type de données PyArrow
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# Effectuez diverses opérations
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
