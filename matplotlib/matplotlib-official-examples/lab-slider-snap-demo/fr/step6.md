# Créer la fonction de mise à jour

Dans cette étape, vous allez créer la fonction de mise à jour pour les curseurs. Cette fonction mettra à jour le tracé lorsque les valeurs des curseurs sont modifiées.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
