# Criar o Gráfico Matplotlib

Nesta etapa, criaremos um gráfico Matplotlib que exibirá nossos dados. Começaremos criando uma figura e adicionando um subplot.

```python
fig = Figure(figsize=(6, 4))
self.canvas = FigureCanvas(fig)
vbox.pack_start(self.canvas, True, True, 0)
ax = fig.add_subplot()
```
