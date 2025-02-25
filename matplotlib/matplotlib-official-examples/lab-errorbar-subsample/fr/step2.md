# Tracer toutes les barre d'erreur

Ensuite, nous allons tracer toutes les barre d'erreur en utilisant la fonction `errorbar` sans aucun sous-échantillonnage. Cela servira de tracé de base pour nous.

```python
fig, ax = plt.subplots()

ax.set_title('Toutes les barre d\'erreur')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
