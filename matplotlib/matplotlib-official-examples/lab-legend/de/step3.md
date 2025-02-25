# Erstellen des Diagramms

Jetzt sind wir bereit, unser Diagramm zu erstellen. Wir werden die `plot`-Funktion von Matplotlib verwenden, um drei Linien auf dem gleichen Graphen zu zeichnen, wobei jeder eine vordefinierte Bezeichnung hat. Wir werden das `label`-Parameter verwenden, um den Bezeichnungen jeder Linie zuzuweisen.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```
