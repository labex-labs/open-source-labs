# フォント内のグリフを表示する

このステップでは、指定されたフォントファイル内のすべてのグリフを標準出力に表示する関数`print_glyphs`を定義します。

```python
import os
import unicodedata
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def print_glyphs(path):
    """
    指定されたフォントファイル内のすべてのグリフを標準出力に表示します。

    パラメータ
    ----------
    path : str or None
        フォントファイルへのパス。Noneの場合、Matplotlibのデフォルトフォントを使用します。
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # デフォルトフォント。

    font = FT2Font(path)

    charmap = font.get_charmap()
    max_indices_len = len(str(max(charmap.values())))

    print("このフォントフェイスには次のグリフが含まれています:")
    for char_code, glyph_index in charmap.items():
        char = chr(char_code)
        name = unicodedata.name(
                char,
                f"{char_code:#x} ({font.get_glyph_name(glyph_index)})")
        print(f"{glyph_index:>{max_indices_len}} {char} {name}")
```
