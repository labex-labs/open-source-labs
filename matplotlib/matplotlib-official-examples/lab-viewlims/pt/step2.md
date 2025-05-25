# Criar a classe UpdatingRect

Criaremos uma subclasse de Rectangle chamada UpdatingRect. Esta classe é chamada com uma instância de Axes, fazendo com que o retângulo atualize sua forma para corresponder aos limites do Axes.

```python
class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
```
