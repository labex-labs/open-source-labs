# 色フィルタ関数を定義する

次に、色フィルタ名に基づいて色フィルタ関数を作成する関数を定義します。この関数は、色フィルタ名に基づいて入力画像を別の色空間に変換するために、colorspacious モジュールを使用します。

```python
def _get_color_filter(name):
    """
    色フィルタ名を指定すると、色フィルタ関数を作成します。

    パラメータ
    ----------
    name : str
        色フィルタ名で、以下のいずれかです。

        - ``"none"``:...
        - ``"greyscale"``: 入力を輝度に変換します。
        - ``"deuteranopia"``: 最も一般的な赤緑型色覚異常をシミュレートします。
        - ``"protanopia"``: まれな赤緑型色覚異常をシミュレートします。
        - ``"tritanopia"``: まれな青黄色型色覚異常をシミュレートします。

        色変換には `colorspacious`_ を使用します。

    戻り値
    -------
    callable
        次の形式の色フィルタ関数です。

        def filter(input: np.ndarray[M, N, D])-> np.ndarray[M, N, D]

        ここで、(M, N) は画像の寸法で、D は色深度 (RGB の場合は 3、RGBA の場合は 4) です。アルファはそのまま通過し、それ以外の場合は無視されます。
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
