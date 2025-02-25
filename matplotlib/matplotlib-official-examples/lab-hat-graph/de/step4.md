# Hut-Graphen erstellen

In diesem Schritt werden wir den Hut-Graphen mit den in dem vorherigen Schritt vorbereiteten Daten und der `hat_graph`-Funktion erstellen.

```python
fig, ax = plt.subplots()
hat_graph(ax, xlabels, [playerA, playerB], ['Player A', 'Player B'])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Spiele')
ax.set_ylabel('Punkte')
ax.set_ylim(0, 60)
ax.set_title('Punkte nach Anzahl von Spielen und Spielern')
ax.legend()

fig.tight_layout()
plt.show()
```
