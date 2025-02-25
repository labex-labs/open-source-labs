# Décaler les axes

Nous allons déplacer les axes gauche et inférieur vers l'extérieur de 10 points à l'aide de la fonction `set_position()`. L'argument de `set_position()` est un tuple avec deux éléments. Le premier élément représente la position de l'axe, et le second élément représente la distance entre l'axe et la zone de tracé.

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
