# 라이브러리 가져오기

이 단계에서는 아이리스 데이터셋에서 결정 경계를 시각화하는 데 필요한 라이브러리를 가져옵니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.datasets import load_iris
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    AdaBoostClassifier,
)
from sklearn.tree import DecisionTreeClassifier
```
