# Sous-échantillonnage des barre d'erreur toutes les 6ème

Maintenant, appliquons le sous-échantillonnage des barre d'erreur pour tracer seulement toutes les 6ème barre d'erreur. Nous pouvons le faire en utilisant le paramètre `errorevery` de la fonction `errorbar`.

```python
fig, ax = plt.subplots()

ax.set_title('Toutes les 6ème barre d\'erreur')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
