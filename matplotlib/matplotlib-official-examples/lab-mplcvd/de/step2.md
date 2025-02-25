# Definieren der Farbfilterfunktion

Als nächstes definieren wir eine Funktion, die eine Farbfilterfunktion basierend auf dem Namen des Farbfilters erstellt. Diese Funktion verwendet das colorspacious-Modul, um das Eingabebild in einen anderen Farbraum basierend auf dem Namen des Farbfilters umzuwandeln.

```python
def _get_color_filter(name):
    """
    Gegeben einen Namen für einen Farbfilter, erstellt eine Farbfilterfunktion.

    Parameter
    ----------
    name : str
        Der Name des Farbfilters, einer der folgenden:

        - ``"none"``:...
        - ``"greyscale"``: Konvertiert die Eingabe in Helligkeit.
        - ``"deuteranopia"``: Simuliert die häufigste Form von Rot-Grün-Farbenblindheit.
        - ``"protanopia"``: Simuliert eine seltnere Form von Rot-Grün-Farbenblindheit.
        - ``"tritanopia"``: Simuliert die seltene Form von Blau-Gelb-Farbenblindheit.

        Farbkonvertierungen verwenden `colorspacious`_.

    Rückgabe
    -------
    callable
        Eine Farbfilterfunktion der Form:

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        wobei (M, N) die Bilddimensionen sind und D die Farbtiefe (3 für RGB, 4 für RGBA). Alpha wird unverändert weitergeleitet und sonst ignoriert.
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
