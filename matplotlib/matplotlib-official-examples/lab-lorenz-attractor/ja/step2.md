# ローレンツ関数の定義

3 つのパラメータを受け取り、3 つの値の配列を返すローレンツ関数を定義します。ローレンツパラメータには、デフォルト値 `s=10`、`r=28`、`b=2.667` を使用します。

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    パラメータ
    ----------
    xyz : array-like, shape (3,)
       3 次元空間内の関心点。
    s, r, b : float
       ローレンツアトラクターを定義するパラメータ。

    戻り値
    -------
    xyz_dot : array, shape (3,)
       *xyz* におけるローレンツアトラクターの偏導関数の値。
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
