# Den Plot erstellen

Jetzt können wir den Plot mithilfe der `plt.subplots()`-Funktion erstellen. Wir werden auch drei Linien mithilfe der `ax.plot()`-Funktion erstellen.

```python
fig, ax = plt.subplots()

# Verwenden von set_dashes() und set_capstyle() zum Ändern der Gestricheltheit einer bestehenden Linie.
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt Linie, 2pt Pause, 10pt Linie, 2pt Pause.
line1.set_dash_capstyle('round')

# Verwenden von plot(..., dashes=...) zum Festlegen der Gestricheltheit beim Erstellen einer Linie.
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

# Verwenden von plot(..., dashes=..., gapcolor=...) zum Festlegen der Gestricheltheit und
# des alternierenden Farbverlaufs beim Erstellen einer Linie.
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')

ax.legend(handlelength=4)
plt.show()
```
