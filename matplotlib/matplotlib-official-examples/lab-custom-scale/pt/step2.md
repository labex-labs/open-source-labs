# Definir a classe MercatorLatitudeScale

Em seguida, definiremos a classe `MercatorLatitudeScale` que implementará a escala personalizada. Esta classe herdará de `mscale.ScaleBase`.

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Escala dados no intervalo de -pi/2 a pi/2 (-90 a 90 graus) usando
    o sistema usado para escalar latitudes em uma projeção de Mercator.

    A função de escala:
      ln(tan(y) + sec(y))

    A função de escala inversa:
      atan(sinh(y))

    Como a escala de Mercator tende ao infinito em +/- 90 graus,
    há um limite definido pelo usuário, acima e abaixo do qual nada
    será plotado. Isso é definido por padrão como +/- 85 graus.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
