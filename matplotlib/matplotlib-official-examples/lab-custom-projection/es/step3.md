# Crear la clase HammerAxes

Crearemos una clase personalizada para la proyección Aitoff-Hammer, una proyección de mapa de área igual llamada `HammerAxes`.

```python
class HammerAxes(GeoAxes):
    """
    Una clase personalizada para la proyección Aitoff-Hammer, una proyección de mapa de área igual.

    https://en.wikipedia.org/wiki/Hammer_projection
    """

    # La proyección debe especificar un nombre. Esto se utilizará por el
    # usuario para seleccionar la proyección,
    # es decir, ``subplot(projection='custom_hammer')``.
    name = 'custom_hammer'

    class HammerTransform(Transform):
        """La transformada base de Hammer."""
        input_dims = output_dims = 2

        def __init__(self, resolution):
            """
            Crea una nueva transformada de Hammer. La resolución es el número de pasos
            para interpolar entre cada segmento de línea de entrada para aproximar su
            trayectoria en el espacio curvo de Hammer.
            """
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, ll):
            longitud, latitud = ll.T

            # Pre-calculamos algunos valores
            mitad_longitud = longitud / 2
            coseno_latitud = np.cos(latitud)
            raiz2 = np.sqrt(2)

            alfa = np.sqrt(1 + coseno_latitud * np.cos(mitad_longitud))
            x = (2 * raiz2) * (coseno_latitud * np.sin(mitad_longitud)) / alfa
            y = (raiz2 * np.sin(latitud)) / alfa
            return np.column_stack([x, y])

        def transform_path_non_affine(self, path):
            # vertices = path.vertices
            ipath = path.interpolado(self._resolution)
            return Path(self.transform(ipath.vertices), ipath.codes)

        def inverted(self):
            return HammerAxes.InvertedHammerTransform(self._resolution)

    class InvertedHammerTransform(Transform):
        input_dims = output_dims = 2

        def __init__(self, resolution):
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, xy):
            x, y = xy.T
            z = np.sqrt(1 - (x / 4) ** 2 - (y / 2) ** 2)
            longitud = 2 * np.arctan((z * x) / (2 * (2 * z ** 2 - 1)))
            latitud = np.arcsin(y*z)
            return np.column_stack([longitud, latitud])

        def inverted(self):
            return HammerAxes.HammerTransform(self._resolution)

    def __init__(self, *args, **kwargs):
        self._longitude_cap = np.pi / 2.0
        super().__init__(*args, **kwargs)
        self.set_aspect(0.5, adjustable='box', anchor='C')
        self.clear()

    def _get_core_transform(self, resolution):
        return self.HammerTransform(resolution)
```
