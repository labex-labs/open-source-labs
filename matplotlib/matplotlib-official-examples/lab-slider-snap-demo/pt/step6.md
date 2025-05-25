# Criar a Função de Atualização

Nesta etapa, você criará a função de atualização para os _sliders_. Esta função atualizará o gráfico quando os valores dos _sliders_ forem alterados.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
