# 데이터셋 로드

다음으로, 작업할 데이터셋을 로드합니다. 이 연습에서는 원하는 데이터셋을 사용할 수 있습니다.

```python
from sklearn.datasets import load_iris

# 아이리스 데이터셋 로드
iris = load_iris()

# 데이터를 특징 (features) 과 목표 (target) 로 분할
X = iris.data
y = iris.target
```
