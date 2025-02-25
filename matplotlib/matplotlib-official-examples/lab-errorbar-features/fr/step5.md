# Tracer les variables avec des barre d'erreur asymétriques

Ensuite, nous allons tracer nos données avec des barre d'erreur asymétriques variables. La fonction `ax.errorbar()` est utilisée à nouveau, mais cette fois le paramètre `xerr` est utilisé pour spécifier les valeurs d'erreur asymétriques.

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
