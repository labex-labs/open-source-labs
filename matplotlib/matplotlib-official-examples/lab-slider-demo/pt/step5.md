# Criar a Função de Atualização

Agora criaremos a função que atualizará a onda senoidal toda vez que ajustarmos os sliders. A função receberá os valores dos sliders de amplitude e frequência e atualizará a onda senoidal de acordo.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
