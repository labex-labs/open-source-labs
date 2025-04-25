# フォントテーブルを描画する

このステップでは、指定されたフォントの最初の 255 文字のフォントテーブルを描画する関数`draw_font_table`を定義します。

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    指定されたフォントの最初の 255 文字のフォントテーブルを描画します。

    パラメータ
    ----------
    path : str or None
        フォントファイルへのパス。None の場合、Matplotlib のデフォルトフォントを使用します。
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # デフォルトフォント。

    font = FT2Font(path)

    # フォントのチャーマップを取得する
    codes = font.get_charmap().items()

    # テーブルのラベルとセルを作成する
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # Matplotlib の Axes.table を使ってテーブルを描画する
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_title(os.path.basename(path))
    ax.set_axis_off()

    table = ax.table(
        cellText=chars,
        rowLabels=labelr,
        colLabels=labelc,
        rowColours=["palegreen"] * 16,
        colColours=["palegreen"] * 16,
        cellColours=[[".95" for c in range(16)] for r in range(16)],
        cellLoc='center',
        loc='upper left',
    )

    # テーブルセルのフォントを指定されたパスのフォントに設定する
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # テーブルの独自のインデックスに注意...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
