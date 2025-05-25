# 데이터셋 로드

다음으로, scikit-learn 의 `load_iris()` 함수를 사용하여 아이리스 데이터셋을 로드합니다. 그런 다음 특징 (X) 과 대상 (y) 변수를 분리합니다.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
