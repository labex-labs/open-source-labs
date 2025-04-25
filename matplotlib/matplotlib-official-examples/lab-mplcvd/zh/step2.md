# 定义颜色滤镜函数

接下来，我们定义一个函数，该函数根据颜色滤镜名称创建一个颜色滤镜函数。此函数使用 `colorspacious` 模块根据颜色滤镜名称将输入图像转换为不同的颜色空间。

```python
def _get_color_filter(name):
    """
    给定一个颜色滤镜名称，创建一个颜色滤镜函数。

    参数
    ----------
    name : str
        颜色滤镜名称，以下之一：

        - ``"none"``:...
        - ``"greyscale"``: 将输入转换为亮度。
        - ``"deuteranopia"``: 模拟最常见的红绿色盲形式。
        - ``"protanopia"``: 模拟一种较罕见的红绿色盲形式。
        - ``"tritanopia"``: 模拟罕见的蓝黄色盲形式。

        颜色转换使用 `colorspacious`_。

    返回
    -------
    callable
        一个颜色滤镜函数，其形式为：

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        其中 (M, N) 是图像尺寸，D 是颜色深度（RGB 为 3，RGBA 为 4）。透明度通道直接传递，其他情况下忽略。
    """
    if name not in _MENU_ENTRIES:
        raise ValueError(f"不支持的滤镜名称：{name!r}")
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
