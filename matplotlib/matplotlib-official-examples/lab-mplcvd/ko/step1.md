# 필요한 라이브러리 및 모듈 가져오기

먼저 Matplotlib, NumPy, colorspacious 를 포함하여 필요한 라이브러리와 모듈을 가져와야 합니다. 또한 시뮬레이션하려는 색상 필터 옵션을 설정합니다.

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
