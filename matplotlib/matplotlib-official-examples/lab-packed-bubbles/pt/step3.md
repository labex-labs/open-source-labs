# Definir a Classe `BubbleChart`

A classe `BubbleChart` é usada para criar o gráfico de bolhas empacotadas. A classe recebe um array de áreas de bolhas e um valor de espaçamento entre as bolhas. O método `__init__` configura as posições iniciais das bolhas e calcula a distância máxima de passo (maximum step distance), que é a distância que cada bolha pode se mover em uma única iteração.

```python
class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Configuração para o colapso das bolhas.

        Parâmetros
        ----------
        area : array-like
            Área das bolhas.
        bubble_spacing : float, default: 0
            Espaçamento mínimo entre as bolhas após o colapso.

        Notas
        -----
        Se "area" estiver ordenado, os resultados podem parecer estranhos.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # calculate initial grid layout for bubbles
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()
```
