# Générer un ensemble de données de classification binaire

Ensuite, nous allons générer un ensemble de données de classification binaire à l'aide de la fonction `make_classification` fournie par scikit-learn. Cette fonction nous permet de spécifier le nombre d'échantillons, de caractéristiques, de grappes par classe et de caractéristiques informatives. Nous utiliserons une valeur d'état aléatoire fixe pour garantir la reproductibilité.

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```
