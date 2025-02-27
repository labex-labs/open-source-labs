# Calificar las muestras

Después de ajustar el estimador, podemos usar el método `score_samples` para calcular la log-verosimilitud de las muestras bajo la función de densidad estimada. Esto nos dará una medida de qué tan probable es cada muestra de acuerdo con la estimación de densidad.

```python
scores = kde.score_samples(X)
```
