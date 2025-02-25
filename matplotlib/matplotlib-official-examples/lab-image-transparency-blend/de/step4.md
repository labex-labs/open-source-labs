# Verwenden von Transparenz, um Werte hervorzuheben

Schließlich werden wir das gleiche Diagramm neu erstellen, aber diesmal verwenden wir Transparenz, um die Extremwerte in den Daten hervorzuheben. Dies wird oft verwendet, um Datenpunkte mit kleineren p-Werten hervorzuheben. Wir werden auch Konturlinien hinzufügen, um die Bildwerte zu betonen.

```python
# Erstelle einen Alphakanal basierend auf den Gewichts-Werten
alphas = Normalize(0,.3, clip=True)(np.abs(weights))
alphas = np.clip(alphas,.4, 1)  # alpha-Wert wird unten bei.4 abgeschnitten

# Erstelle die Figur und das Bild
fig, ax = plt.subplots()
ax.imshow(greys)
ax.imshow(weights, alpha=alphas, **imshow_kwargs)

# Füge Konturlinien hinzu, um verschiedene Ebenen weiter hervorzuheben.
ax.contour(weights[::-1], levels=[-.1,.1], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()

ax.contour(weights[::-1], levels=[-.0001,.0001], colors='k', linestyles='-')
ax.set_axis_off()
plt.show()
```
