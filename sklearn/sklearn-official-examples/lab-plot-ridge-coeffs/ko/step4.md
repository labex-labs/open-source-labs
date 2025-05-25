# 서로 다른 정규화 강도로 모델 학습

반복문을 사용하여 서로 다른 정규화 강도로 모델을 학습합니다. `set_params` 함수에서 alpha 값을 변경하여 정규화 강도를 설정합니다. 각 alpha 값에 대한 계수와 오차를 저장합니다.

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```
