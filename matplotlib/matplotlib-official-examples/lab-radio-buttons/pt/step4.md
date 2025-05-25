# Adicionar Funcionalidade aos Botões de Rádio

Agora, adicionaremos funcionalidade aos botões de rádio usando a função `on_clicked()`. Definiremos duas funções - `hzfunc()` e `colorfunc()` - que serão chamadas quando os botões de rádio forem clicados.

```python
def hzfunc(label):
    hzdict = {'1 Hz': s0, '2 Hz': s1, '4 Hz': s2}
    ydata = hzdict[label]
    l.set_ydata(ydata)
    fig.canvas.draw()
radio.on_clicked(hzfunc)

rax = fig.add_axes([0.05, 0.4, 0.15, 0.15], facecolor=axcolor)
radio2 = RadioButtons(
    rax, ('red', 'blue', 'green'),
    label_props={'color': ['red', 'blue', 'green']},
    radio_props={
        'facecolor': ['red', 'blue', 'green'],
        'edgecolor': ['darkred', 'darkblue', 'darkgreen'],
    })


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw()
radio2.on_clicked(colorfunc)

rax = fig.add_axes([0.05, 0.1, 0.15, 0.15], facecolor=axcolor)
radio3 = RadioButtons(rax, ('-', '--', '-.', ':'))


def stylefunc(label):
    l.set_linestyle(label)
    fig.canvas.draw()
radio3.on_clicked(stylefunc)
```
