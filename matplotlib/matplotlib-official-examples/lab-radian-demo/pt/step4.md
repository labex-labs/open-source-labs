# Plotar dados no primeiro subplot

Plote o cosseno dos valores de x no primeiro subplot usando a função `plot` de `matplotlib.pyplot`. Use o parâmetro `xunits` para especificar que o eixo x deve estar em radianos.

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
