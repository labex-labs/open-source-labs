# Импортируем необходимые библиотеки и модули

Во - первых, нам нужно импортировать необходимые библиотеки и модули, в том числе Matplotlib, NumPy и colorspacious. Также задаем параметры фильтрации цветов, которые мы хотим имитировать.

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
