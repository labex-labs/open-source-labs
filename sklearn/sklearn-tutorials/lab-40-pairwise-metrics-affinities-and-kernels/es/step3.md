# Similaridad Coseno

La similitud coseno es una medida de la similitud entre dos vectores. Calcula el coseno del ángulo entre los vectores después de normalizarlos.

Scikit-learn proporciona la función `cosine_similarity` para calcular la similitud coseno entre vectores.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Salida:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
