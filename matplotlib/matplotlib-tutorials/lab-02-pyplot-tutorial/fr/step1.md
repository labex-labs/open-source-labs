# Générer un graphique simple

Pour commencer, générons un graphique simple à l'aide de la fonction `plot` dans `pyplot`. Dans cet exemple, nous allons tracer un graphique en ligne avec les valeurs y `[1, 2, 3, 4]` :

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

Explication :

- Nous importons le module `pyplot` de `matplotlib` et le redéfinissons sous le nom `plt`.
- La fonction `plot` est utilisée pour générer un graphique en ligne. En fournissant une seule liste de valeurs y, les valeurs x sont automatiquement générées comme étant `[0, 1, 2, 3]`, car les plages Python commencent à 0.
- La fonction `ylabel` définit l'étiquette pour l'axe y.
- Enfin, la fonction `show` affiche le graphique.
