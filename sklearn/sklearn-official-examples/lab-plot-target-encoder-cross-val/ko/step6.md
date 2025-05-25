# 교차 검증을 사용한 선형 모델 계수 평가

선형 모델의 계수를 살펴보면, 대부분의 가중치가 정보적인 특징인 0 번 열의 특징에 집중되어 있습니다. 교차 검증을 사용하여 선형 모델의 계수를 평가하는 코드는 다음과 같습니다.

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```
