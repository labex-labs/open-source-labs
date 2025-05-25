# Criar os botões `Next` e `Previous`

Agora, criaremos os botões `Next` e `Previous` usando a função `add_axes` do `matplotlib.pyplot` e atribuiremos as funções de callback que criamos anteriormente a eles usando `on_clicked`.

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
