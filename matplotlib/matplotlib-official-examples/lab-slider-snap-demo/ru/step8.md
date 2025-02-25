# Создать кнопку сброса

В этом шаге вы создадите кнопку сброса для ползунков. При нажатии кнопка сброса установит значения ползунков в их исходные.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```