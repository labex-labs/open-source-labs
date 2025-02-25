# Импортируем библиотеки и получаем стили рамок

В этом шаге мы импортируем необходимые библиотеки и получаем стили рамок, которые будем использовать для построения графиков.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```
