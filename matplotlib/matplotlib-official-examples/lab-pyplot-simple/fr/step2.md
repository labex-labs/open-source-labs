# Créez un graphique simple

Pour créer un graphique simple avec Matplotlib, vous devez fournir une liste de nombres que vous souhaitez tracer. Dans ce cas, nous allons tracer une liste de nombres en fonction de leur indice, ce qui donnera une ligne droite. Utilisez une chaîne de format (ici, 'o-r') pour définir les marqueurs (cercles), le style de ligne (ligne continue) et la couleur (rouge).

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.ylabel('certains nombres')
plt.show()
```
