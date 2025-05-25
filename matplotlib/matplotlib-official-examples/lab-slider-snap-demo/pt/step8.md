# Criar o Botão de Reset

Nesta etapa, você criará um botão de _reset_ para os _sliders_. Quando clicado, o botão de _reset_ redefinirá os valores dos _sliders_ para seus valores iniciais.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
