# Zeige den Graphen an

Sobald du alle Textobjekte erstellt und angepasst hast, kannst du den Graphen mit `plt.show()` anzeigen. Der folgende Codeblock zeigt den vollständigen Code für den Graphen.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# Das erste Wort, erstellt mit text().
text = ax.text(.1,.5, "Matplotlib", color="red")
# Folgende Wörter, positioniert mit annotate(), relativ zum vorherigen.
text = ax.annotate(
    " sagt,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # benutzerdefinierte Eigenschaften
text = ax.annotate(
    " hallo", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # benutzerdefinierte Eigenschaften
text = ax.annotate(
    " Welt!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # benutzerdefinierte Eigenschaften

plt.show()
```
