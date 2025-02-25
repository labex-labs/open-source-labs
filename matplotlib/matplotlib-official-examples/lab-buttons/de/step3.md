# Erstelle die Button-Callback-Funktionen

Jetzt werden wir zwei Callback-Funktionen für die Schaltflächen **Next** und **Previous** erstellen. Diese Funktionen werden das Diagramm mit einer neuen Sinuswelle mit einer anderen Frequenz aktualisieren.

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```
