# Импортируем библиотеки и задаем случайный сид

Начнем с импорта необходимых библиотек и установки случайного сид для воспроизводимости результатов.

```python
import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.rcParams['font.size'] = 8.0

# Fixing random state for reproducibility
np.random.seed(19680801)
```
