# Étiquetage avec un titre

Si nous voulons que l'étiquette soit alignée avec le titre, nous pouvons l'incorporer dans le titre ou utiliser l'argument clé `loc`.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
