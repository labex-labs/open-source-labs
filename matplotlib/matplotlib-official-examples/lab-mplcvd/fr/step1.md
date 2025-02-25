# Importez les bibliothèques et les modules nécessaires

Tout d'abord, nous devons importer les bibliothèques et les modules nécessaires, notamment Matplotlib, NumPy et colorspacious. Nous définissons également les options de filtre de couleur que nous souhaitons simuler.

```python
import functools
from pathlib import Path

import colorspacious

import numpy as np

_BUTTON_NAME = "Filter"
_BUTTON_HELP = "Simuler les déficiences de la vision colorée"
_MENU_ENTRIES = {
    "None": None,
    "Greyscale": "greyscale",
    "Deuteranopia": "deuteranomaly",
    "Protanopia": "protanomaly",
    "Tritanopia": "tritanomaly",
}
```
