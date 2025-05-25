# 필요한 라이브러리 가져오기

이 실습에서는 다음 라이브러리를 사용합니다: `pandas`, `numpy`, `matplotlib`, `sklearn.datasets`, `RandomForestClassifier`, `randint`, 그리고 `HalvingRandomSearchCV`. 다음 코드를 사용하여 가져옵니다.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingRandomSearchCV
```
