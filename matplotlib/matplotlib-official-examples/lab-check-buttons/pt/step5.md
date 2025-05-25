# Definir Função de Callback

Precisamos definir uma função de _callback_ para os botões de seleção. Esta função será chamada toda vez que um botão de seleção for clicado. Usaremos esta função para alternar a visibilidade da linha correspondente no gráfico.

```python
def callback(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    ln.figure.canvas.draw_idle()

check.on_clicked(callback)
```
