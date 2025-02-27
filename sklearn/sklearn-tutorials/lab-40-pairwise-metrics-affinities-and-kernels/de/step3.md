# Cosinusähnlichkeit

Die Cosinusähnlichkeit ist ein Maß für die Ähnlichkeit zwischen zwei Vektoren. Sie berechnet den Kosinus des Winkels zwischen den Vektoren, nachdem diese normalisiert wurden.

Scikit-learn bietet die Funktion `cosine_similarity` an, um die Cosinusähnlichkeit zwischen Vektoren zu berechnen.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Ausgabe:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
