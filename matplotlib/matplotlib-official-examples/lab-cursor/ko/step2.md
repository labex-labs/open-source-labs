# 데이터 생성

이 단계에서는 numpy 를 사용하여 임의의 데이터 포인트를 생성합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data points
x, y = 4*(np.random.rand(2, 100) - .5)
```
