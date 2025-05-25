# 등가선형 및 선형 회귀 모델 적합

이제 생성된 데이터에 등가선형 회귀 모델과 선형 회귀 모델을 모두 적합합니다.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # LinearRegression 을 위해 x 를 2 차원으로 변환해야 함
```
