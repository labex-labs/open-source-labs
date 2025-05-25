# 아이리스 데이터셋 로드

Scikit-learn 의 내장 함수 `load_iris`를 사용하여 아이리스 데이터셋을 로드합니다.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # 처음 두 개의 특징만 가져옵니다.
y = iris.target
```
