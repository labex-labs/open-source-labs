# Formatierung des Diagrammstils

Als nächstes passen wir den Stil unseres Diagramms an. Wir können das optionale dritte Argument der `plot`-Funktion verwenden, um die Formatzeichenfolge anzugeben, die die Farbe und den Linientyp des Diagramms angibt. Beispielsweise erstellen wir das gleiche Liniendiagramm mit roten Kreisen:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

Erklärung:

- Wir verwenden die Formatzeichenfolge `'ro'`, um roten Kreise für das Diagramm anzugeben.
- Die `axis`-Funktion wird verwendet, um die Anzeigebereich der Achsen festzulegen, indem der Wertebereich für die x- und y-Achse angegeben wird.
