# Création de la classe HammerAxes

Nous allons créer une classe personnalisée pour la projection Aitoff-Hammer, une projection cartographique à aire égale appelée `HammerAxes`.

```python
class HammerAxes(GeoAxes):
    """
    Une classe personnalisée pour la projection Aitoff-Hammer, une projection cartographique
    à aire égale.

    https://en.wikipedia.org/wiki/Hammer_projection
    """

    # La projection doit spécifier un nom. Celui-ci sera utilisé par
    # l'utilisateur pour sélectionner la projection,
    # c'est-à-dire ``subplot(projection='custom_hammer')``.
    name = 'custom_hammer'

    class HammerTransform(Transform):
        """La transformation de base de Hammer."""
        input_dims = output_dims = 2

        def __init__(self, resolution):
            """
            Crée une nouvelle transformation de Hammer. La résolution est le nombre d'étapes
            pour interpoler entre chaque segment de ligne d'entrée pour approximer son
            trajet dans l'espace courbe de Hammer.
            """
            Transform.__init__(self)
            self._resolution = resolution

        def transform_non_affine(self, ll):
            longitude, latitude = ll.T

            # Pré-calculer quelques valeurs
            demi_longitude = longitude / 2
            cos_latitude = np.cos(latitude)
            racine_deux = np.sqrt(2)

            alpha = np.sqrt(1 + cos_latitude * np.cos(demi_longitude))
            x = (2 * racine_deux) * (cos_latitude * np.sin(demi_longitude)) / alpha
            y = (racine_deux * np.sin(latitude)) / alpha
            return np.column_stack([x, y])

        def transform_path_non_affine(self, path):
            # vertices = path.vertices
            ipath = path.interpolé(self._resolution)
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
