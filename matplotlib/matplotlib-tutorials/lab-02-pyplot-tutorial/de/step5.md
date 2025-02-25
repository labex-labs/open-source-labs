# Anpassen von Linieneigenschaften

Matplotlib ermöglicht es Ihnen, verschiedene Linieneigenschaften anzupassen, wie die Linienstärke, der Strichstil und die Farbe. Zeigen wir einige Möglichkeiten, um Linieneigenschaften zu setzen:

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Verwenden der Setter-Methode der Line2D-Instanz
line.set_linewidth(2.0)  # Setze die Linienstärke-Eigenschaft der Linie auf 2.0

# Verwenden der plt.setp-Funktion
plt.setp(line, color='r', linewidth=2.0)  # Setze die Farbe und die Linienstärke-Eigenschaften mit der setp-Funktion

plt.show()
```

Erklärung:

- Wir erstellen ein Array `x` und berechnen die entsprechenden y-Werte mit der `np.sin`-Funktion.
- Die `plot`-Funktion wird aufgerufen, um einen Liniendiagramm zu erstellen.
- Wir verwenden die `set`-Methode der `Line2D`-Instanz, um die Linienstärke-Eigenschaft der Linie auf 2.0 zu setzen.
- Alternativ können wir die `setp`-Funktion verwenden, um mehrere Eigenschaften der Linie, wie Farbe und Linienstärke, mit Schlüsselwortargumenten zu setzen.
