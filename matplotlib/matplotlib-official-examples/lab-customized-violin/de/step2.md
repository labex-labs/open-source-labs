# Erstellen eines standardmäßigen Violindiagramms

Als nächstes werden wir ein standardmäßiges Violindiagramm mit der `violinplot`-Funktion von Matplotlib erstellen. Dies wird als Vergleichsbasis dienen, wenn wir das Diagramm in späteren Schritten anpassen.

```python
# create default violin plot
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
