# Générer un ensemble de données

Nous allons générer un ensemble de données à 3 classes en utilisant la fonction `make_blobs` de scikit-learn. Nous utiliserons 1000 échantillons et définirons les centres des grappes à `[-5, 0], [0, 1.5], [5, -1]`. Nous transformerons ensuite l'ensemble de données en utilisant une matrice de transformation pour rendre l'ensemble de données plus difficile à classifier.

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
