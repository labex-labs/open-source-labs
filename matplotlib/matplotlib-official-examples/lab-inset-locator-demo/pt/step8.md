# Criar um _Inset_ Centrado em Coordenadas da Figura

Podemos criar um _inset_ que é centralizado horizontalmente em coordenadas da figura e verticalmente limitado para se alinhar com os eixos usando o método `blended_transform_factory()` para criar uma transformação combinada e usá-la como o parâmetro `bbox_transform`.

```python
# Criar um inset centralizado horizontalmente em coordenadas da figura e verticalmente
# limitado para se alinhar com os eixos.
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
