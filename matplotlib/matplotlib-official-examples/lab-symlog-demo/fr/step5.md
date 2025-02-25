# Créer un graphique symlog sur l'axe y

Dans le deuxième sous-graphique, nous allons créer un graphique `symlog` sur l'axe y.

```python
ax1.plot(y1, x)
ax1.set_yscale('symlog')
ax1.set_ylabel('symlogy')
```
