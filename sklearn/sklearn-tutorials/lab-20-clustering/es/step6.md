# Evaluar el clustering

Para evaluar los resultados del clustering, podemos calcular la inercia de los clusters, que representa la suma de las distancias al cuadrado de las muestras a su centro de cluster más cercano.

```python
# Calculate the inertia of the clusters
inertia = kmeans.inertia_
print("Inertia:", inertia)
```
