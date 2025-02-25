# Erstelle die Zurücksetz-Schaltfläche

In diesem Schritt wirst du eine Zurücksetz-Schaltfläche für die Schieberegler erstellen. Wenn die Schaltfläche betätigt wird, wird sie die Werte der Schieberegler auf ihre Anfangswerte zurücksetzen.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
