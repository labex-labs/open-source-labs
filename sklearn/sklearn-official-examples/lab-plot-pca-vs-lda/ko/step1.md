# 데이터셋 로드

먼저, scikit-learn 의 내장 함수 `load_iris()`를 사용하여 아이리스 데이터셋을 로드해야 합니다.

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```
