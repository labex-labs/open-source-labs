# Créer le premier sous-graphique

Nous allons créer le premier sous-graphique avec le paramètre `rstride` défini sur `10` et le paramètre `cstride` défini sur `0`.

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
