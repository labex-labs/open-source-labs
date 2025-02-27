# Evaluar el agrupamiento

Para evaluar el rendimiento del algoritmo de agrupamiento K-Means, podemos calcular la puntuación de inercia. La puntuación de inercia mide la suma de las distancias entre cada punto de datos y el centro de su cluster asignado. Una puntuación de inercia más baja indica un mejor agrupamiento.

```python
print("Inertia Score:", kmeans.inertia_)
```
