# Steuern der Textpositionierung und -stil

Wir können auch die Positionierung und den Stil des Textes in unserem Matplotlib-Graphen steuern. Versuchen Sie, den folgenden Code Ihrem Skript hinzuzufügen:

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

Dies wird vier Textelemente zu unserem Graphen hinzufügen, wobei jeder eine andere Farbe, Schriftgröße und Position hat.
