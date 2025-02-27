# Clasificar las características

Después de ajustar los datos al objeto RFE, podemos clasificar las características según su importancia. Usaremos el atributo `ranking_` del objeto RFE para obtener las clasificaciones de las características. También redimensionaremos las clasificaciones para que coincidan con la forma de las imágenes originales.

```python
ranking = rfe.ranking_.reshape(digits.images[0].shape)
```
