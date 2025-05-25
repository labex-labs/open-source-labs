# Definir Função para Atualizar o Título

Defina a função para atualizar o título da figura com a hora atual.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
