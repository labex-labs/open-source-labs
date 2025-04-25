# 二次 x 軸を作成する

二次 x 軸を作成し、周波数から周期に変換します。順方向の関数として`one_over`を、逆方向の関数として`inverse`を使用します。

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
