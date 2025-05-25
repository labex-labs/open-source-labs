# 필요한 라이브러리 가져오기

먼저, MLPClassifier, MinMaxScaler, datasets, matplotlib.pyplot 등 필요한 라이브러리를 가져와야 합니다. 또한, 학습 중 발생할 수 있는 수렴 경고를 무시하기 위해 ConvergenceWarning 을 가져옵니다.

```python
import warnings

import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
```
