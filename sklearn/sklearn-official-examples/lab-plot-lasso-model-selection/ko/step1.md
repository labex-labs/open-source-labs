# 데이터셋

먼저, `sklearn.datasets`의 `load_diabetes` 함수를 사용하여 당뇨병 데이터셋을 로드합니다. 이 데이터셋은 10 개의 기저 변수 (나이, 성별, 체질량 지수, 평균 혈압, 그리고 6 가지 혈청 측정값) 와 기저 상태 이후 1 년 후 질병 진행 정도의 정량적 측정값으로 구성됩니다.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
