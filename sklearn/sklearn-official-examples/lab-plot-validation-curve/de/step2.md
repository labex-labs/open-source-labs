# Definieren des Hyperparameterbereichs

Wir werden einen Bereich von Werten für den SVM-Kernparametern gamma definieren, den wir testen möchten.

```python
param_range = np.logspace(-6, -1, 5)
```
