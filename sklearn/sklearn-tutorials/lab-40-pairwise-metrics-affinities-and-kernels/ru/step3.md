# Косинусная близость

Косинусная близость - это мера сходства между двумя векторами. Она вычисляет косинус угла между векторами после их нормализации.

Scikit-learn предоставляет функцию `cosine_similarity` для вычисления косинусной близости между векторами.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Результат:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
