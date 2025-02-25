# Tracer les données

Maintenant, nous pouvons tracer nos données à l'aide de la fonction `plot`. Nous allons créer deux lignes à l'aide des données que nous avons créées à l'étape 3.

```python
ax.plot(theta, r, color="tab:orange", lw=3, label="a line")
ax.plot(0.5 * theta, r, color="tab:blue", ls="--", lw=3, label="another line")
```
