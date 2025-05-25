# 데이터셋 로드

첫 번째 단계는 scikit-learn 에서 아이리스 데이터셋을 로드하는 것입니다.

```python
from sklearn.datasets import load_iris

# 데이터셋 로드
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
