# Erstellen des Diagramms und der Radiobuttons

Jetzt werden wir das Diagramm und die Radiobuttons erstellen. Wir werden die `subplots()`-Funktion verwenden, um das Diagramm zu erstellen, und die `RadioButtons()`-Funktion, um die Radiobuttons zu erstellen.

```python
fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color='red')
fig.subplots_adjust(left=0.3)

axcolor = 'lightgoldenrodyellow'
rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('1 Hz', '2 Hz', '4 Hz'),
                     label_props={'color': 'cmy', 'fontsize': [12, 14, 16]},
                     radio_props={'s': [16, 32, 64]})
```
