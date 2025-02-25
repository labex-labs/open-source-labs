# Masquer les axes supérieur et droit

Nous allons maintenant masquer les axes supérieur et droit, car nous n'avons besoin que des axes gauche et inférieur.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```
