# Afficher le graphique

Une fois que vous avez créé et personnalisé tous les objets de texte, vous pouvez afficher le graphique à l'aide de `plt.show()`. Le bloc de code suivant montre le code complet pour le graphique.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# Le premier mot, créé avec text().
text = ax.text(.1,.5, "Matplotlib", color="red")
# Les mots suivants, positionnés avec annotate(), par rapport au précédent.
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # propriétés personnalisées
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # propriétés personnalisées
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # propriétés personnalisées

plt.show()
```
