# Créer la fonction de mise à jour

Nous allons maintenant créer la fonction qui mettra à jour l'onde sinusoïdale chaque fois que nous ajustons les curseurs. La fonction prendra les valeurs des curseurs d'amplitude et de fréquence et mettra à jour l'onde sinusoïdale en conséquence.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
