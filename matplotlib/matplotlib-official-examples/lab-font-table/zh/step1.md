# 打印字体中的字形

在这一步中，我们将定义一个函数 `print_glyphs`，它会将给定字体文件中的所有字形打印到标准输出。

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    将给定字体文件中的所有字形打印到标准输出。

    参数
    ----------
    path : str 或 None
        字体文件的路径。如果为 None，则使用 Matplotlib 的默认字体。
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # 默认字体。

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("字体包含以下字形：")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
