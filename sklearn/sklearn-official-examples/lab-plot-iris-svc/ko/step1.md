# 필요한 라이브러리 가져오기 및 데이터셋 로드

```python
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.inspection import DecisionBoundaryDisplay

# 사용할 데이터 가져오기
iris = datasets.load_iris()
# 처음 두 개의 특징만 사용합니다. 2 차원 데이터셋을 사용하여 이 부분을 피할 수 있습니다.
X = iris.data[:, :2]
y = iris.target
```
