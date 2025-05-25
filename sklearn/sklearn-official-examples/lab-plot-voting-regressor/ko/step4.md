# 예측 수행

이제 각 회귀 모델을 사용하여 처음 20 개 데이터에 대한 예측을 수행합니다.

```python
# 예측 수행
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```
