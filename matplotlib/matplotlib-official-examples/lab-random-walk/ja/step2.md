# ランダムウォーク関数を定義する

与えられたステップ数と最大ステップサイズでランダムウォークを生成する関数を定義します。この関数は2つの入力を受け取ります。`num_steps`はランダムウォークの合計ステップ数で、`max_step`は各ステップの最大サイズです。ステップの乱数を生成するために`numpy.random`を、最終位置を取得するためにステップの累積和を計算するために`numpy.cumsum`を使用します。

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```
