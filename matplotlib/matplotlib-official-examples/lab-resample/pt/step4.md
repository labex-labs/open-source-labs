# Atualizando os dados

Definiremos um método `update` que atualizará os dados. O método receberá `ax` (eixo) como um parâmetro de entrada. Atualizaremos a linha obtendo o limite de visualização e verificando se a largura do limite de visualização é diferente de delta. Se a largura do limite de visualização for diferente de delta, atualizaremos o delta e obteremos `xstart` e `xend`. Em seguida, definiremos os dados para os dados com _downsample_ e desenharemos o _idle_.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
