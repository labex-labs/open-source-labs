# Ajouter du texte au graphique

Vous pouvez ajouter du texte à votre graphique à l'aide de la fonction `ax.text()`. Dans cet exemple, nous allons ajouter du texte avec différentes familles de polices.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ n'est pas $\mu$")
```
