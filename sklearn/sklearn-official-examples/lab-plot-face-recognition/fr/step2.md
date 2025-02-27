# Charger et explorer l'ensemble de données

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

Nous téléchargeons l'ensemble de données à l'aide de la fonction `fetch_lfw_people()` de scikit-learn. Nous explorons ensuite l'ensemble de données en obtenant le nombre d'échantillons, la hauteur et la largeur des images. Nous obtenons également les données d'entrée `X`, la cible `y`, les noms de cibles `target_names` et le nombre de classes `n_classes`.
