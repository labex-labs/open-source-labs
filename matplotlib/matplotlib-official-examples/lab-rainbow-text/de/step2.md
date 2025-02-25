# Weitere Textobjekte erstellen

Der nächste Schritt besteht darin, die weiteren Textobjekte mit `~.Axes.annotate` zu erstellen. Mit dieser Funktion kannst du die Textobjekte relativ zum vorherigen Textobjekt positionieren. Der folgende Code erstellt drei Textobjekte, die rechts vom vorherigen Textobjekt positioniert sind.

```python
text = ax.annotate(
    " sagt,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # benutzerdefinierte Eigenschaften
text = ax.annotate(
    " hallo", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # benutzerdefinierte Eigenschaften
text = ax.annotate(
    " Welt!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # benutzerdefinierte Eigenschaften
```
