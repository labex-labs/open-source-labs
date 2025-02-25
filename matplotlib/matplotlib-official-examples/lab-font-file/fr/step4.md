# Spécifiez la police pour le titre

Nous spécifions la police pour le titre du tracé en utilisant la méthode `set_title()` de la classe `Axes`. Nous passons le chemin de la police en tant que paramètre `font` et le nom du fichier de police en tant que titre du tracé.

```python
ax.set_title(f'This is a special font: {fpath.name}', font=fpath)
```
