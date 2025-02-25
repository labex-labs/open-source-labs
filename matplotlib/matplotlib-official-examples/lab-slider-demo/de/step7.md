# Erstellen der Zurücksetz-Schaltfläche

Wir werden nun eine Zurücksetz-Schaltfläche erstellen, die die Schieberegler auf ihre Anfangswerte zurücksetzt.

```python
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)
```
