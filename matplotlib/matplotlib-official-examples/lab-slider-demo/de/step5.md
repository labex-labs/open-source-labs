# Erstellen der Aktualisierungsfunktion

Wir werden nun die Funktion erstellen, die die Sinuswelle jedes Mal aktualisiert, wenn wir die Schieberegler anpassen. Die Funktion nimmt die Werte der Amplitude- und Frequenz-Schieberegler entgegen und aktualisiert die Sinuswelle entsprechend.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
