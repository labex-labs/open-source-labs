# Импортируем необходимые библиотеки и создаем фигуру с подграфиками

Начнем с импорта необходимых библиотек и создания фигуры с подграфиками.

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
```
