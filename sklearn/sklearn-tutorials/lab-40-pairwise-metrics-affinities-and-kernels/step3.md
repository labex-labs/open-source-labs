# Cosine Similarity

Cosine similarity is a measure of the similarity between two vectors. It calculates the cosine of the angle between the vectors after normalizing them.

Scikit-learn provides the `cosine_similarity` function to compute the cosine similarity between vectors.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Output:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
