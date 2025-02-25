# Création de barre d'erreur pour theta se chevauchant

Dans cette étape, nous allons créer des barre d'erreur pour theta se chevauchant pour démontrer comment elles peuvent réduire la lisibilité du graphique de sortie.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```
