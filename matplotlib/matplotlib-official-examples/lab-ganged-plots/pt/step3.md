# Criar Subplots

Criamos três subplots usando a função `subplots` em Matplotlib. Definimos o parâmetro `sharex` como `True` para garantir que os subplots compartilhem um eixo x comum. Também removemos o espaço vertical entre os subplots usando a função `subplots_adjust`.

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
