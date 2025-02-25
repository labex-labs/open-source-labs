# Definir la clase BubbleChart

La clase `BubbleChart` se utiliza para crear el gráfico de burbujas empaquetadas. La clase recibe una matriz de áreas de burbujas y un valor de espaciado entre burbujas. El método `__init__` configura las posiciones iniciales de las burbujas y calcula la distancia máxima de paso, que es la distancia que cada burbuja puede moverse en una sola iteración.

```python
class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Configuración para el colapso de las burbujas.

        Parámetros
        ----------
        area : array-like
            Área de las burbujas.
        bubble_spacing : float, valor predeterminado: 0
            Espaciado mínimo entre las burbujas después del colapso.

        Notas
        -----
        Si "area" está ordenado, los resultados pueden verse extraños.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # calcular el diseño de cuadrícula inicial para las burbujas
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()
```
