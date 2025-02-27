# Импортируем необходимые модули

Сначала нам нужно импортировать необходимые модули из библиотеки scikit-learn. Мы будем использовать класс `SimpleImputer` для одномерной (унивариатной) импуттации признаков и класс `IterativeImputer` для многомерной (мультивариатной) импуттации признаков.

```python
import numpy as np
from sklearn.impute import SimpleImputer, IterativeImputer
```
