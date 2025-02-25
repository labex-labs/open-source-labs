# Ajoutez des étiquettes et la mise en forme

Nous allons ajouter des étiquettes aux patches du diagramme Sankey en utilisant l'attribut `text` de chaque patch. Nous allons également formater le texte pour qu'il soit en gras et augmenter la taille de la police.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
