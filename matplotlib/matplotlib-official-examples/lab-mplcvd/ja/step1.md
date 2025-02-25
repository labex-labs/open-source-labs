# 必要なライブラリとモジュールをインポートする

まず、Matplotlib、NumPy、およびcolorspaciousを含む必要なライブラリとモジュールをインポートする必要があります。また、シミュレートしたい色フィルタオプションを設定します。

```python
import functools
from pathlib import Path

import colorspacious

import numpy as np

_BUTTON_NAME = "Filter"
_BUTTON_HELP = "Simulate color vision deficiencies"
_MENU_ENTRIES = {
    "None": None,
    "Greyscale": "greyscale",
    "Deuteranopia": "deuteranomaly",
    "Protanopia": "protanomaly",
    "Tritanopia": "tritanomaly",
}
```
