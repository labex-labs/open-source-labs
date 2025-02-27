# Crear pesos de muestra

Crearemos dos conjuntos de pesos de muestra. El primer conjunto de pesos de muestra será constante para todos los puntos, y el segundo conjunto de pesos de muestra será mayor para algunos valores atípicos.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
