# Criar Classe HammerAxes

Criaremos uma classe personalizada para a projeção Aitoff-Hammer, uma projeção de mapa de área igual chamada `HammerAxes`.

```python
class HammerAxes(GeoAxes):
    """
    Uma classe personalizada para a projeção Aitoff-Hammer, uma projeção de mapa de área igual.

    https://en.wikipedia.org/wiki/Hammer_projection
    """

    # A projeção deve especificar um nome. Isso será usado pelo
    # usuário para selecionar a projeção,
    # i.e. ``subplot(projection='custom_hammer')``.
    name = 'custom_hammer'

    class HammerTransform(Transform):
        """A transformação Hammer base."""
        input_dims = output_dims = 2

        def __init__(self, resolution):
            """
            Cria uma nova transformação Hammer. Resolução é o número de passos
            para interpolar entre cada segmento de linha de entrada para aproximar seu
            caminho no espaço Hammer curvo.
            """
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, ll):
            longitude, latitude = ll.T

            # Pré-calcular alguns valores
            half_long = longitude / 2
            cos_latitude = np.cos(latitude)
            sqrt2 = np.sqrt(2)

            alpha = np.sqrt(1 + cos_latitude * np.cos(half_long))
            x = (2 * sqrt2) * (cos_latitude * np.sin(half_long)) / alpha
            y = (sqrt2 * np.sin(latitude)) / alpha
            return np.column_stack([x, y])

        def transform_path_non_affine(self, path):
            # vertices = path.vertices
            ipath = path.interpolated(self._resolution)
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
            longitude = 2 * np.arctan((z * x) / (2 * (2 * z ** 2 - 1)))
            latitude = np.arcsin(y*z)
            return np.column_stack([longitude, latitude])

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
