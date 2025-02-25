# Erstellen eines einfachen Sankey-Diagramms

Wir beginnen mit der Erstellung eines einfachen Sankey-Diagramms, das zeigt, wie die Sankey-Klasse verwendet wird.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'Erster', 'Zweiter', 'Dritter', 'Vierter', 'Fünfter'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("Die Standardeinstellungen erzeugen ein Diagramm wie dieses.")
```

Dieser Code erzeugt ein Sankey-Diagramm mit Standardeinstellungen, die die Beschriftungen und Orientierungen der Ströme umfassen. Das resultierende Diagramm wird mit dem Titel "Die Standardeinstellungen erzeugen ein Diagramm wie dieses." angezeigt.
