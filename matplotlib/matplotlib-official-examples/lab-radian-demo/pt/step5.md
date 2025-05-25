# Plotar dados no segundo subplot

Plote o cosseno dos valores de x no segundo subplot usando a função `plot` de `matplotlib.pyplot`. Use o parâmetro `xunits` para especificar que o eixo x deve estar em graus.

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
