# Créer le graphe de flèches

Avec la grille et la direction des flèches définies, nous pouvons créer le graphe de flèches. Dans cet exemple, nous utiliserons la fonction `quiver` de Matplotlib pour créer le tracé. Le paramètre `length` définit la longueur des flèches et le paramètre `normalize` normalise les flèches à une longueur de 1.

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
