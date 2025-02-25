# Erstellen einer Figur und Festlegen alternativer Cursor

Als nächstes erstellen wir eine Figur und legen für jedes Subplot mit einer Schleife die alternativen Cursor fest. Wir fügen auch Text zu jedem Subplot hinzu, um den verwendeten Cursor anzuzeigen.

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Hover over an Axes to see alternate Cursors')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```
