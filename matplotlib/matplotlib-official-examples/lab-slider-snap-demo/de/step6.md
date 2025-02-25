# Erstelle die Aktualisierungsfunktion

In diesem Schritt wirst du die Aktualisierungsfunktion für die Schieberegler erstellen. Diese Funktion wird das Diagramm aktualisieren, wenn die Werte der Schieberegler geändert werden.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
