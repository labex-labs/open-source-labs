# An die Datenpunkte anhaften

Der im vorherigen Schritt erstellte Cursor ist immer noch etwas langsam, da die Cursorposition bei jeder Mausbewegung aktualisiert wird. In diesem Schritt werden wir einen Cursor erstellen, der an die Datenpunkte eines `Line2D`-Objekts anhaftet.

```python
class SnappingCursor:
    """
    Ein Kreuzhaarschirmcursor, der an den Datenpunkt einer Linie anhaftet, der
    am nächsten an die *x*-Position des Cursors liegt.

    Aus Gründen der Einfachheit wird hier vorausgesetzt, dass die *x*-Werte der Daten sortiert sind.
    """
    def __init__(self, ax, line):
        self.ax = ax
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        self.x, self.y = line.get_data()
        self._last_index = None
        # Textposition in Achsenkoordinaten
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible()!= visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw

    def on_mouse_move(self, event):
        if not event.inaxes:
            self._last_index = None
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.draw()
        else:
            self.set_cross_hair_visible(True)
            x, y = event.xdata, event.ydata
            index = min(np.searchsorted(self.x, x), len(self.x) - 1)
            if index == self._last_index:
                return  # noch am selben Datenpunkt. Keine Aktion erforderlich.
            self._last_index = index
            x = self.x[index]
            y = self.y[index]
            # Aktualisierung der Linienpositionen
            self.horizontal_line.set_ydata([y])
            self.vertical_line.set_xdata([x])
            self.text.set_text(f'x={x:1.2f}, y={y:1.2f}')
            self.ax.figure.canvas.draw()

x = np.arange(0, 1, 0.01)
y = np.sin(2 * 2 * np.pi * x)

fig, ax = plt.subplots()
ax.set_title('Anhaftender Cursor')
line, = ax.plot(x, y, 'o')
snap_cursor = SnappingCursor(ax, line)
fig.canvas.mpl_connect('motion_notify_event', snap_cursor.on_mouse_move)

plt.show()
```
