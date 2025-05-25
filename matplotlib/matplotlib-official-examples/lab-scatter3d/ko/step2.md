# 데이터 설정

NumPy 라이브러리를 사용하여 임의의 값으로 두 개의 데이터 세트를 생성합니다. 한 세트는 x 및 y 좌표를 나타내고, 다른 세트는 z 좌표를 나타냅니다.

```python
def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
