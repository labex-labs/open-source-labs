# 데이터 생성

NumPy 를 사용하여 임의의 데이터를 생성합니다.

```python
np.random.seed(19680801)
X = np.random.rand(100, 200)
xs = np.mean(X, axis=1)
ys = np.std(X, axis=1)
```
