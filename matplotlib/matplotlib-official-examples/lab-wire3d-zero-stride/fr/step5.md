# Créer le second sous-graphique

Nous allons créer le second sous-graphique avec le paramètre `rstride` défini sur `0` et le paramètre `cstride` défini sur `10`.

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
