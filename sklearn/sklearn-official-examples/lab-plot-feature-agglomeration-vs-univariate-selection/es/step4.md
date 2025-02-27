# Calcular los coeficientes de un Bayesian Ridge con GridSearch

```python
cv = KFold(2)  # generador de validación cruzada para la selección del modelo
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```
