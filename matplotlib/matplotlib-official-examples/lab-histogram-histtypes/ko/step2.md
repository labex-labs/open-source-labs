# 무작위 데이터 생성

NumPy 의 `random.normal` 함수를 사용하여 두 개의 무작위 데이터 세트를 생성합니다. 이 세트는 서로 다른 스타일의 히스토그램을 만드는 데 사용됩니다.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
