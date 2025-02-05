# 导入必要的库和模块

首先，我们需要导入必要的库和模块，包括 Matplotlib、NumPy 和 colorspacious。我们还设置了想要模拟的颜色滤镜选项。

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
