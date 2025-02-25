# Crear el botón de restablecimiento

En este paso, creará un botón de restablecimiento para los deslizadores. Cuando se haga clic en él, el botón de restablecimiento restablecerá los valores de los deslizadores a sus valores iniciales.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
