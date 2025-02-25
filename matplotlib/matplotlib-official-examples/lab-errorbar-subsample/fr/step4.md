# Décaler la deuxième série de 3

Dans certains cas, nous pouvons vouloir appliquer le sous-échantillonnage des barre d'erreur à différentes parties de nos données. Nous pouvons le faire en spécifiant un tuple pour le paramètre `errorevery`. Par exemple, appliquons le sous-échantillonnage des barre d'erreur à la deuxième série, mais la décalons de 3 points de données.

```python
fig, ax = plt.subplots()

ax.set_title('Deuxième série décalée de 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
