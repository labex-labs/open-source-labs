# Anpassen und Speichern des Diagramms

Wir können das Diagramm mit den Anpassungsmöglichkeiten von Matplotlib weiter anpassen. Wir können das Diagramm auch in eine Datei speichern.

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ Konzentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
