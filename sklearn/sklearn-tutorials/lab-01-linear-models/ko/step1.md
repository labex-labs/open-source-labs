# 최소 제곱법

> 머신 러닝에 대한 사전 경험이 없으시면 [지도 학습: 회귀](https://labex.io/courses/supervised-learning-regression)를 참고하세요.

최소 제곱법 (OLS) 은 관측된 목표값과 예측된 목표값 간의 제곱 차이 합을 최소화하는 선형 회귀 방법입니다. 수학적으로 다음과 같은 형태의 문제를 해결합니다:
$$\min_{w} || X w - y||_2^2$$

선형 회귀 모델을 OLS 를 사용하여 적합해 보겠습니다.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- scikit-learn 에서 `linear_model` 모듈을 가져옵니다.
- `LinearRegression`의 인스턴스를 생성합니다.
- `fit` 메서드를 사용하여 모델을 학습 데이터에 적합시킵니다.
- 선형 모델의 계수를 출력합니다.
