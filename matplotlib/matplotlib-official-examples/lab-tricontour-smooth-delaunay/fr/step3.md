# Générer des points de données de test

Nous générons un ensemble de points de données de test aléatoires, avec des valeurs de x et y comprises entre -1 et 1. Nous générons également un ensemble correspondant de valeurs de z à l'aide de la fonction `experiment_res` définie à l'étape 2.

```python
# Paramètres utilisateur pour les points de données de test

# Nombre de points de données de test, testé de 3 à 5000 pour subdiv=3
n_test = 200

# Points aléatoires
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
