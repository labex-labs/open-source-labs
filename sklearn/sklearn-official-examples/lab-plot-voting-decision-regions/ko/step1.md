# 데이터 로드

Scikit-Learn 의 `datasets` 모듈을 사용하여 아이리스 데이터셋을 로드합니다. 꽃받침 길이와 꽃잎 길이 두 가지 특징만 사용합니다.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
