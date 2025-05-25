# Configurar a Classe Scope

A classe Scope conterá os dados e métodos que precisamos para criar o osciloscópio. No construtor, inicializamos as variáveis necessárias e configuramos o gráfico.

```python
class Scope:
    def __init__(self, ax, maxt=2, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
```
