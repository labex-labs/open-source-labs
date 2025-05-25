# 보조 X 축 생성

이제 보조 x 축을 생성하고 주파수 (frequency) 에서 주기 (period) 로 변환합니다. 순방향 함수로 `one_over`를 사용하고 역방향 함수로 `inverse`를 사용합니다.

```python
def one_over(x):
    """Vectorized 1/x, treating x==0 manually"""
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x

# the function "1/x" is its own inverse
inverse = one_over

secax = ax.secondary_xaxis('top', functions=(one_over, inverse))
secax.set_xlabel('period [s]')
```
