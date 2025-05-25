# Criar uma Figura e Conectar o Evento de Fechamento

Nesta etapa, criaremos uma figura e conectaremos o evento de fechamento à função `on_close` definida na Etapa 1. Isso é feito usando o método `mpl_connect` do canvas da figura.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
