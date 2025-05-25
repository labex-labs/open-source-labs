# 아이리스 데이터셋 로드

scikit-learn 라이브러리에서 아이리스 데이터셋을 로드합니다. 이 데이터셋은 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비의 네 가지 특징을 포함합니다. 이진 분류를 위해 처음 두 특징만 사용할 것입니다.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 2] # 이진 분류를 위해 처음 두 특징만 사용
y = y[y != 2]

X /= X.max() # 수렴 속도를 높이기 위해 X 를 정규화합니다.
```
