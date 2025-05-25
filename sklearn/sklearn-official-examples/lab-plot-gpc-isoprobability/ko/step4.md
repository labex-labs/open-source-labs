# 모델 평가

학습된 GPC 모델의 분류 성능을 평가할 것입니다. 점들의 그리드를 생성하고 학습된 모델을 사용하여 각 점에 대한 예측 확률을 계산할 것입니다.

```python
# 실제 함수와 예측 확률 평가
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```
