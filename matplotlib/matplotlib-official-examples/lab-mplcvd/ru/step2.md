# Определяем функцию фильтрации цветов

Далее мы определяем функцию, которая создает функцию фильтрации цветов на основе имени фильтра цвета. Эта функция использует модуль colorspacious для преобразования входного изображения в другое цветовое пространство в зависимости от имени фильтра цвета.

```python
def _get_color_filter(name):
    """
    По заданному имени фильтра цвета создается функция фильтрации цветов.

    Параметры
    ----------
    name : str
        Имя фильтра цвета, одно из следующих:

        - ``"none"``:...
        - ``"greyscale"``: Преобразует входное изображение в яркость.
        - ``"deuteranopia"``: Имитирует наиболее распространенную форму красно-зеленого
          Daltonизма.
        - ``"protanopia"``: Имитирует более редкую форму красно-зеленого Daltonизма.
        - ``"tritanopia"``: Имитирует редкую форму сине-желтого Daltonизма.

        Преобразования цветов используют `colorspacious`_.

    Возвращает
    -------
    callable
        Функция фильтрации цветов, имеющая следующую форму:

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        где (M, N) - размеры изображения, а D - глубина цвета (3 для RGB, 4 для RGBA).
        Альфа-канал передается без изменений и в остальном игнорируется.
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
