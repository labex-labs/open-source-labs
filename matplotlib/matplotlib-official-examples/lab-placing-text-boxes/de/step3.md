# Hinzufügen einer Textbox mit Statistiken

Nachdem wir nun ein einfaches Histogramm haben, verbessern wir es, indem wir eine Textbox hinzufügen, die die statistischen Informationen zu unseren Daten anzeigt. Dies macht die Visualisierung für die Betrachter informativer.

## Erstellen des Textinhalts

Zunächst müssen wir den Textinhalt vorbereiten, der in unsere Textbox eingefügt werden soll. Geben Sie in einer neuen Zelle den folgenden Code ein und führen Sie ihn aus:

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

Dieser Code erstellt einen mehrzeiligen String, der den Mittelwert, Median und die Standardabweichung unserer Daten enthält. Betrachten wir einige interessante Aspekte dieses Codes:

1. Die Methode `\n'.join(...)` verbindet mehrere Strings mit einem Zeilenumbruch dazwischen.
2. Das `r` vor jedem String macht ihn zu einem "raw" String, was nützlich ist, wenn man Sonderzeichen einfügt.
3. Die Notation `$...$` wird für LaTeX-stilige mathematische Formatierung in matplotlib verwendet.
4. `\mu` und `\sigma` sind LaTeX-Symbole für die griechischen Buchstaben μ (mu) und σ (sigma).
5. `%.2f` ist ein Formatierungs-Spezifizierer, der eine Fließkommazahl mit zwei Dezimalstellen anzeigt.

## Erstellen und Hinzufügen der Textbox

Jetzt erstellen wir unser Histogramm erneut und fügen die Textbox hinzu. Geben Sie in einer neuen Zelle den folgenden Code ein und führen Sie ihn aus:

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

Wenn Sie diese Zelle ausführen, sollten Sie Ihr Histogramm mit einer Textbox in der oberen linken Ecke sehen, die die Statistiken anzeigt.

## Verständnis des Codes für die Textbox

Lassen Sie uns die wichtigen Teile des Codes, der die Textbox erstellt, analysieren:

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`:

   - Dies erstellt ein Wörterbuch mit Eigenschaften für die Textbox.
   - `boxstyle='round'`: Macht die Ecken der Box abgerundet.
   - `facecolor='wheat'`: Setzt die Hintergrundfarbe der Box auf Weizenfarbe.
   - `alpha=0.5`: Macht die Box halbtransparent (50 % Deckkraft).

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`:
   - Dies fügt Text an der Position (0.05, 0.95) in den Achsen hinzu.
   - `transform=ax.transAxes`: Dies ist wichtig - es bedeutet, dass die Koordinaten in Achsen-Einheiten (0 - 1) statt in Daten-Einheiten sind. Also bedeutet (0.05, 0.95) "5 % von der linken Kante und 95 % von der unteren Kante des Diagramms".
   - `fontsize=14`: Setzt die Schriftgröße.
   - `verticalalignment='top'`: Richtet den Text so aus, dass die Oberkante des Texts an der angegebenen y-Koordinate liegt.
   - `bbox=properties`: Wendet unsere Textbox-Eigenschaften an.

Die Textbox bleibt relativ zu den Diagrammachsen an der gleichen Position, auch wenn Sie in das Diagramm hineinzoomen oder den Datenbereich ändern. Dies liegt daran, dass wir `transform=ax.transAxes` verwendet haben, das Achsen-Koordinaten anstelle von Daten-Koordinaten nutzt.
