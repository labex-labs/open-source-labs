# 분류기 정의

이 단계에서는 OLS 및 Ridge 회귀 분류기를 정의합니다.

```python
classifiers = dict(
    ols=linear_model.LinearRegression(), ridge=linear_model.Ridge(alpha=0.1)
)
```
