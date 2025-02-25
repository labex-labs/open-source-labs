# データの作成

このステップでは、プロットするためのデータを作成します。異なる周波数のサイン波とコサイン波を生成するために、`squiggle_xy` 関数を使用します。

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
