# Créer les objets de texte suivants

L'étape suivante consiste à créer les objets de texte suivants à l'aide de `~.Axes.annotate`. Cette fonction vous permet de positionner l'objet de texte par rapport à l'objet de texte précédent. Le code suivant crée trois objets de texte qui sont positionnés à droite de l'objet de texte précédent.

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # propriétés personnalisées
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # propriétés personnalisées
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # propriétés personnalisées
```
