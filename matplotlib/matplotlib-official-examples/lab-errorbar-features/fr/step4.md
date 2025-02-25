# Tracer les variables avec des barre d'erreur symétriques

Nous allons maintenant tracer nos données avec des barre d'erreur symétriques variables. La fonction `ax.errorbar()` est utilisée pour créer le tracé, et le paramètre `yerr` est utilisé pour spécifier les valeurs d'erreur.

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
