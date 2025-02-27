# Ajouter une légende

Nous allons ajouter une légende au tracé à l'aide de la fonction `legend` de `matplotlib.pyplot`. Nous définirons les étiquettes sur `"non pondéré"` et `"pondéré"` respectivement.

```python
plt.legend(
    [disp.surface_.collections[0], wdisp.surface_.collections[0]],
    ["non weighted", "weighted"],
    loc="upper right",
)
```
