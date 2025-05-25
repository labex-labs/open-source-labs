# 필요한 라이브러리 가져오기

먼저, 필요한 라이브러리를 가져와야 합니다. 머신 러닝 및 데이터 전처리를 위해 scikit-learn 라이브러리를 사용할 것입니다.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
```
