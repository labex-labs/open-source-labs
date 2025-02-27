# Similarité cosinus

La similarité cosinus est une mesure de la similarité entre deux vecteurs. Elle calcule le cosinus de l'angle entre les vecteurs après les avoir normalisés.

Scikit-learn fournit la fonction `cosine_similarity` pour calculer la similarité cosinus entre des vecteurs.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Sortie :

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
