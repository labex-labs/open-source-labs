# Enregistrez le graphique

Enfin, nous pouvons enregistrer notre graphique sur le disque. Suivez ces étapes :

1. Affichez les formats de fichier pris en charge à l'aide de `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Enregistrez la figure sous forme de fichier image à l'aide de `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Désactivez le commentaire de cette ligne pour enregistrer la figure.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

Vous pouvez ouvrir le fichier image enregistré à l'aide de l'explorateur de fichiers dans la barre latérale gauche.
