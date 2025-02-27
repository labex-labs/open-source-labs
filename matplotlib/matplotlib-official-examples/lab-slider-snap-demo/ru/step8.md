# Создание кнопки сброса

На этом этапе вы создадите кнопку сброса для ползунков. При нажатии кнопки сброса значения ползунков будут возвращены к их начальным значениям.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
