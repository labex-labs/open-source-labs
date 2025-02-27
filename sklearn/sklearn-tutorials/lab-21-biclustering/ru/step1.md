# Импортируем необходимые библиотеки и датасет

Сначала импортируем необходимые библиотеки и загрузим примерный датасет, который мы будем использовать для бикластеризации.

```python
import numpy as np
from sklearn.cluster import SpectralCoclustering, SpectralBiclustering

# Load sample data
data = np.arange(100).reshape(10, 10)
```
