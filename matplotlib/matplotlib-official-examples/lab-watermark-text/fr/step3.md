# Ajouter un filigrane de texte

Pour ajouter un filigrane de texte, nous pouvons utiliser la méthode `text()` de l'objet `Figure`. Nous devons fournir la position, le texte et d'autres propriétés telles que la taille de police, la couleur et la transparence.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```
