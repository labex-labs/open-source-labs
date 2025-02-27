# Ajuster le régresseur Huber

Nous allons maintenant ajuster le HuberRegressor à l'ensemble de données. Nous allons ajuster le modèle pour une plage de valeurs d'epsilon pour montrer comment la fonction de décision approche celle de la régression Ridge à mesure que la valeur d'epsilon augmente.

```python
# Définir la plage de valeurs pour epsilon
epsilon_values = [1, 1.5, 1.75, 1.9]

# Définir les valeurs de x pour le tracé
x = np.linspace(X.min(), X.max(), 7)

# Définir les couleurs pour le tracé
colors = ["r-", "b-", "y-", "m-"]

# Ajuster le régresseur Huber pour une série de valeurs d'epsilon.
for k, epsilon in enumerate(epsilon_values):
    huber = HuberRegressor(alpha=0.0, epsilon=epsilon)
    huber.fit(X, y)
    coef_ = huber.coef_ * x + huber.intercept_
    plt.plot(x, coef_, colors[k], label="huber loss, %s" % epsilon)

# Ajouter une légende au tracé
plt.legend(loc=0)

# Afficher le tracé
plt.title("HuberRegressor avec différentes valeurs d'epsilon")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
