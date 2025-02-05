# 绘制字体表

在这一步中，我们将定义一个函数 `draw_font_table`，用于绘制给定字体的前 255 个字符的字体表。

```python
import os
from pathlib import Path
import unicodedata
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ft2font import FT2Font

def draw_font_table(path):
    """
    绘制给定字体的前 255 个字符的字体表。

    参数
    ----------
    path : str 或 None
        字体文件的路径。如果为 None，则使用 Matplotlib 的默认字体。
    """
    if path is None:
        path = fm.findfont(fm.FontProperties())  # 默认字体。

    font = FT2Font(path)

    # 获取字体的字符映射表
    codes = font.get_charmap().items()

    # 创建表格的标签和单元格
    labelc = [f"{i:X}" for i in range(16)]
    labelr = [f"{i:02X}" for i in range(0, 16*16, 16)]
    chars = [["" for c in range(16)] for r in range(16)]

    for char_code, glyph_index in codes:
        if char_code >= 256:
            continue
        row, col = divmod(char_code, 16)
        chars[row][col] = chr(char_code)

    # 使用 Matplotlib 的 Axes.table 绘制表格
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

    # 将表格单元格的字体设置为给定路径的字体
    for key, cell in table.get_celld().items():
        row, col = key
        if row > 0 and col > -1:  # 注意表格特殊的索引方式...
            cell.set_text_props(font=Path(path))

    fig.tight_layout()
    plt.show()
```
