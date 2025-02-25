# Nächstes Shading, Gitter mit derselben Form

Normalerweise bedeutet das Weglassen einer Zeile und Spalte von Daten nicht, was der Benutzer meint, wenn er `X`, `Y` und `Z` alle die gleiche Form hat. Für diesen Fall erlaubt Matplotlib `shading='nearest'` und zentriert die gefärbten Vierecke auf den Gitterpunkten. Wenn ein Gitter mit der falschen Form mit `shading='nearest'` übergeben wird, wird ein Fehler ausgelöst. Wir können das Gitter mit dem folgenden Codeblock visualisieren:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
