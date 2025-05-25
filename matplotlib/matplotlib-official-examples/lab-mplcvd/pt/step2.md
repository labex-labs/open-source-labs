# Definir a função de filtro de cores

Em seguida, definimos uma função que cria uma função de filtro de cores com base no nome do filtro de cores. Esta função usa o módulo colorspacious para converter a imagem de entrada para um espaço de cores diferente com base no nome do filtro de cores.

```python
def _get_color_filter(name):
    """
    Dado um nome de filtro de cores, cria uma função de filtro de cores.

    Parâmetros
    ----------
    name : str
        O nome do filtro de cores, um dos seguintes:

        - ``"none"``: ...
        - ``"greyscale"``: Converte a entrada para luminosidade.
        - ``"deuteranopia"``: Simula a forma mais comum de daltonismo vermelho-verde.
        - ``"protanopia"``: Simula uma forma mais rara de daltonismo vermelho-verde.
        - ``"tritanopia"``: Simula a rara forma de daltonismo azul-amarelo.

        As conversões de cores usam `colorspacious`_.

    Retorna
    -------
    callable
        Uma função de filtro de cores que tem a forma:

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        onde (M, N) são as dimensões da imagem, e D é a profundidade de cor (3 para
        RGB, 4 para RGBA). Alpha é passado inalterado e, caso contrário,
        ignorado.
    """
    if name not in _MENU_ENTRIES:
        raise ValueError(f"Unsupported filter name: {name!r}")
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
