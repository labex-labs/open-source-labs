# 교차 검증 없이 선형 모델 계수 평가

Ridge 모델이 과적합되는 이유는 정보적인 특징에 비해 극단적으로 높은 카디널리티를 가진 특징에 더 많은 가중치를 할당하기 때문입니다. 교차 검증 없이 선형 모델의 계수를 평가하는 코드는 다음과 같습니다.

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
