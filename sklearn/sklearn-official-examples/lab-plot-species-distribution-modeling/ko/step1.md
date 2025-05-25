# 라이브러리 가져오기

이 단계에서는 분석에 필요한 라이브러리를 가져옵니다. 머신 러닝을 위해 scikit-learn 라이브러리, 수치 계산을 위해 numpy 라이브러리, 시각화를 위해 matplotlib 라이브러리를 가져올 것입니다.

```python
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import Bunch
from sklearn.datasets import fetch_species_distributions
from sklearn import svm, metrics
```
