# 필요한 라이브러리 가져오기

필요한 라이브러리를 가져오는 것으로 시작합니다. `sklearn.datasets`에서 `make_gaussian_quantiles`와 `accuracy_score`를, `sklearn.ensemble`에서 `AdaBoostClassifier`와 `DecisionTreeClassifier`를, 그리고 `matplotlib.pyplot`를 가져옵니다.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
```
