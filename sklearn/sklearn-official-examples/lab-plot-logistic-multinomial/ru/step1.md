# Импорт библиотек

Начнем с импорта необходимых библиотек для этого практического занятия. Мы будем использовать библиотеку scikit-learn для генерации датасета и обучения моделей логистической регрессии, а библиотеку matplotlib для построения границы решения.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```
