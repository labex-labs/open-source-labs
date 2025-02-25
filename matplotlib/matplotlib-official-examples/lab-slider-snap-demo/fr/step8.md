# Créer le bouton de réinitialisation

Dans cette étape, vous allez créer un bouton de réinitialisation pour les curseurs. Lorsqu'il est cliqué, le bouton de réinitialisation remettra les valeurs des curseurs à leurs valeurs initiales.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
