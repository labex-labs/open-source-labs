# Définissez la fonction de filtre de couleur

Ensuite, nous définissons une fonction qui crée une fonction de filtre de couleur en fonction du nom du filtre de couleur. Cette fonction utilise le module colorspacious pour convertir l'image d'entrée dans un espace de couleur différent en fonction du nom du filtre de couleur.

```python
def _get_color_filter(name):
    """
    Étant donné un nom de filtre de couleur, crée une fonction de filtre de couleur.

    Paramètres
    ----------
    name : str
        Le nom du filtre de couleur, l'un des suivants :

        - ``"none"``:...
        - ``"greyscale"``: Convertissez l'entrée en luminosité.
        - ``"deuteranopia"``: Simulez la forme la plus courante de daltonisme rouge-vert.
        - ``"protanopia"``: Simulez une forme plus rare de daltonisme rouge-vert.
        - ``"tritanopia"``: Simulez la forme rare de daltonisme bleu-jaune.

        Les conversions de couleur utilisent `colorspacious`_.

    Retours
    -------
    callable
        Une fonction de filtre de couleur qui a la forme :

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        où (M, N) sont les dimensions de l'image et D est la profondeur de couleur (3 pour RGB, 4 pour RGBA). L'alpha est transmis tel quel et sinon ignoré.
    """
    if name not in _MENU_ENTRIES:
        raise ValueError(f"Nom de filtre non pris en charge : {name!r}")
    name = _MENU_ENTRIES[name]

    if name is None:
        return None

    elif name == "greyscale":
        rgb_to_jch = colorspacious.cspace_converter("sRGB1", "JCh")
        jch_to_rgb = colorspacious.cspace_converter("JCh", "sRGB1")

        def convert(im):
            greyscale_JCh = rgb_to_jch(im)
            greyscale_JCh[..., 1] = 0
            im = jch_to_rgb(greyscale_JCh)
            return im

    else:
        cvd_space = {"name": "sRGB1+CVD", "cvd_type": name, "severity": 100}
        convert = colorspacious.cspace_converter(cvd_space, "sRGB1")

    def filter_func(im, dpi):
        alpha = None
        if im.shape[-1] == 4:
            im, alpha = im[..., :3], im[..., 3]
        im = convert(im)
        if alpha is not None:
            im = np.dstack((im, alpha))
        return np.clip(im, 0, 1), 0, 0

    return filter_func
```
