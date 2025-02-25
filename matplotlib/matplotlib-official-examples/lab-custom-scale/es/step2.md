# Definir la clase MercatorLatitudeScale

A continuación, definiremos la clase `MercatorLatitudeScale` que implementará la escala personalizada. Esta clase heredará de `mscale.ScaleBase`.

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Escala los datos en el rango -pi/2 a pi/2 (-90 a 90 grados) utilizando
    el sistema utilizado para escalar las latitudes en una proyección de Mercator__.

    La función de escala:
      ln(tan(y) + sec(y))

    La función de escala inversa:
      atan(sinh(y))

    Dado que la escala de Mercator tiende a infinito en +/- 90 grados,
    existe un umbral definido por el usuario, por encima y por debajo del cual
    no se graficará nada. Esto por defecto es +/- 85 grados.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
