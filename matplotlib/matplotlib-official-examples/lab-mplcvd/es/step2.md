# Definir la función de filtro de color

A continuación, definimos una función que crea una función de filtro de color basada en el nombre del filtro de color. Esta función utiliza el módulo colorspacious para convertir la imagen de entrada a un espacio de color diferente según el nombre del filtro de color.

```python
def _get_color_filter(name):
    """
    Dado el nombre de un filtro de color, crea una función de filtro de color.

    Parámetros
    ----------
    name : str
        El nombre del filtro de color, uno de los siguientes:

        - ``"none"``:...
        - ``"greyscale"``: Convertir la entrada a luminosidad.
        - ``"deuteranopia"``: Simular la forma más común de daltonismo de rojo-verde.
        - ``"protanopia"``: Simular una forma menos común de daltonismo de rojo-verde.
        - ``"tritanopia"``: Simular la forma rara de daltonismo azul-amarillo.

        Las conversiones de color utilizan `colorspacious`_.

    Devuelve
    -------
    callable
        Una función de filtro de color que tiene la forma:

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        donde (M, N) son las dimensiones de la imagen y D es la profundidad de color (3 para RGB, 4 para RGBA). El canal alfa se pasa sin cambios y en caso contrario se ignora.
    """
    if name not in _MENU_ENTRIES:
        raise ValueError(f"Nombre de filtro no admitido: {name!r}")
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
