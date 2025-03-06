# Erstellen eines einfachen Histogramms

Nachdem wir nun unsere Daten haben, erstellen wir ein Histogramm, um deren Verteilung zu visualisieren. Ein Histogramm teilt die Daten in Bins (Intervalle) auf und zeigt die Häufigkeit der Datenpunkte in jedem Bin an.

## Erstellen des Histogramms

Geben Sie in einer neuen Zelle Ihres Jupyter Notebooks den folgenden Code ein und führen Sie ihn aus:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

Wenn Sie diese Zelle ausführen, sollten Sie ein Histogramm sehen, das die Verteilung Ihrer Zufallsdaten anzeigt. Die Ausgabe sollte wie eine glockenförmige Kurve (Normalverteilung) aussehen, die in der Nähe von Null zentriert ist.

## Verständnis des Codes

Lassen Sie uns analysieren, was jede Zeile im Code tut:

1. `fig, ax = plt.subplots(figsize=(10, 6))`: Erstellt ein Figure- und ein Axes-Objekt. Der `figsize`-Parameter legt die Größe des Diagramms in Zoll (Breite, Höhe) fest.

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`: Erstellt ein Histogramm unserer Daten `x` mit 50 Bins. Die Bins sind himmelblau gefärbt und haben schwarze Ränder.

3. `ax.set_title('Distribution of Random Data', fontsize=16)`: Fügt dem Diagramm einen Titel mit einer Schriftgröße von 16 hinzu.

4. `ax.set_xlabel('Value', fontsize=12)` und `ax.set_ylabel('Frequency', fontsize=12)`: Fügen Beschriftungen für die x- und y-Achse mit einer Schriftgröße von 12 hinzu.

5. `plt.tight_layout()`: Passt das Diagramm automatisch an die Figure-Area an.

6. `plt.show()`: Zeigt das Diagramm an.

Das Histogramm zeigt, wie unsere Daten verteilt sind. Da wir `np.random.randn()` verwendet haben, das Daten aus einer Normalverteilung generiert, hat das Histogramm eine Glockenform, die um 0 zentriert ist. Die Höhe jeder Säule gibt an, wie viele Datenpunkte in diesem Bereich liegen.
