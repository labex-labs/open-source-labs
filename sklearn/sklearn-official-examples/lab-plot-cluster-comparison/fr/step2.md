# Génération de jeux de données

Les jeux de données sont générés pour tester et comparer différents algorithmes de clustering. Les jeux de données suivants sont générés :

- Cercles bruités
- Lunes bruitées
- Blobs
- Sans structure
- Données distribuées de manière anisotrope
- Blobs avec des variances variées

```python
n_samples = 500

noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)
```
