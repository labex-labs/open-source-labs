# Création de barre d'erreur pour le rayon important

Dans cette étape, nous allons créer des barre d'erreur pour le rayon important pour démontrer comment elles peuvent entraîner une mise à l'échelle indésirable des données, réduisant la plage affichée.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
