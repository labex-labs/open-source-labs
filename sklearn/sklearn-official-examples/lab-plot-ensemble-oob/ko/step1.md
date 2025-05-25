# 필요한 라이브러리 가져오기

필요한 라이브러리, scikit-learn, NumPy, Matplotlib 등을 가져오는 것으로 시작합니다. 또한 재현성을 보장하기 위해 랜덤 상태 값을 설정합니다.

```python
import matplotlib.pyplot as plt
from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

RANDOM_STATE = 123
```
