# Создание функции обновления

На этом этапе вы создадите функцию обновления для ползунков. Эта функция будет обновлять график при изменении значений ползунков.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
