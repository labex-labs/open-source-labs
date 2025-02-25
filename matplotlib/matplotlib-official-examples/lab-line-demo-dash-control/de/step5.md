# Die Strichfolge mit `.Line2D.set_dashes()` ändern

Wir können die Strichfolge mit `.Line2D.set_dashes()` ändern. In diesem Beispiel ändern wir die Strichfolge für `line1`, um ein Strichmuster von 2pt Linie, 2pt Pause, 10pt Linie und 2pt Pause zu erstellen. Wir setzen auch den Endstil auf 'round' mit `line1.set_dash_capstyle()`.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt Linie, 2pt Pause, 10pt Linie, 2pt Pause.
line1.set_dash_capstyle('round')
```
