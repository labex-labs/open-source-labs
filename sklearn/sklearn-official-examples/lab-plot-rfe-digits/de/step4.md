# Visualisiere die Feature-Bewertungen

Schließlich werden wir die Feature-Bewertungen mit der Matplotlib-Bibliothek darstellen. Wir werden die Funktion `matshow()` verwenden, um die Bewertungen als Bild anzuzeigen. Wir werden auch eine Farbskala und einen Titel zum Diagramm hinzufügen.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```
