# 데이터 로드

이 단계에서는 scikit-learn 의 datasets 모듈을 사용하여 iris 데이터셋을 로드합니다. 데이터셋의 첫 두 개 특징을 선택하여 변수 X 에 할당하고, 대상 변수를 Y 에 할당합니다.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
