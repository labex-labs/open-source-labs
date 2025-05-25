# 데이터셋 로드 및 전처리

scikit-learn 라이브러리를 사용하여 아이리스 데이터셋을 로드합니다. 이 데이터셋은 각각 50 개의 인스턴스를 가진 3 개의 클래스로 구성되어 있으며, 각 클래스는 아이리스 식물의 한 유형을 나타냅니다. 각 인스턴스는 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비의 4 개의 특징을 가지고 있습니다.

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay

# 아이리스 데이터셋 로드
iris = datasets.load_iris()
X = iris.data[:, :2]  # 첫 두 개의 특징만 사용합니다.
Y = iris.target
```
