# Импорт библиотек

Первым шагом является импорт необходимых библиотек. Мы будем импортировать следующие библиотеки:

- numpy
- matplotlib
- sklearn

```python
from joblib import cpu_count
from itertools import cycle
from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

from sklearn.cluster import Birch, MiniBatchKMeans
from sklearn.datasets import make_blobs
```
