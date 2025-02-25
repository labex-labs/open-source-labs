# Ajoutez du texte au tracé

Nous allons ajouter du texte au tracé en utilisant la fonction `ax.text()`. Nous allons ajouter du texte à quatre emplacements différents sur le tracé, chacun avec une famille de polices différente : serif, monospace, sans-serif et cursive.

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```
