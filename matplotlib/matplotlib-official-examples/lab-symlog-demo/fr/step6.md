# Créer un graphique symlog sur l'axe x et l'axe y

Dans le troisième sous-graphique, nous allons créer un graphique `symlog` sur l'axe x et l'axe y. Nous définirons également le paramètre `linthresh` sur 0,015.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
