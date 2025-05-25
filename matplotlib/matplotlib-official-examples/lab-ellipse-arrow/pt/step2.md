# Criar uma Elipse

Em seguida, você precisa criar uma elipse usando a classe `Ellipse`. Você pode especificar o centro da elipse, a largura e a altura da elipse e o ângulo de rotação.

```python
from matplotlib.patches import Ellipse

ellipse = Ellipse(
    xy=(2, 4),
    width=30,
    height=20,
    angle=35,
    facecolor="none",
    edgecolor="b"
)
ax.add_patch(ellipse)
```
