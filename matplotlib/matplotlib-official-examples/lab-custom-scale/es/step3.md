# Implementar la clase MercatorLatitudeTransform

Dentro de la clase `MercatorLatitudeScale`, definiremos la clase `MercatorLatitudeTransform` que realmente transformará los datos. Esta clase heredará de `mtransforms.Transform`.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # Hay dos miembros de valor que deben definirse.
        # ``input_dims`` y ``output_dims`` especifican el número de dimensiones de entrada
        # y dimensiones de salida de la transformación.
        # Estos se utilizan por el marco de transformación para hacer alguna
        # comprobación de errores y evitar que transformaciones incompatibles se
        # conecten juntas. Cuando se definen transformaciones para una
        # escala, que, por definición, son separables y tienen solo una
        # dimensión, estos miembros siempre deben establecerse en 1.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            Esta transformación toma una matriz de numpy y devuelve una copia transformada.
            Dado que el rango de la escala de Mercator está limitado por el
            umbral especificado por el usuario, la matriz de entrada debe estar enmascarada para
            contener solo valores válidos. Matplotlib manejará las matrices enmascaradas
            y eliminará los datos fuera de rango del gráfico. Sin embargo, la
            matriz devuelta *debe* tener la misma forma que la matriz de entrada, ya que
            estos valores deben permanecer sincronizados con los valores en la otra
            dimensión.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Sobrescriba este método para que Matplotlib sepa cómo obtener la
            transformación inversa para esta transformación.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
