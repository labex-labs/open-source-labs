# ランダムウォークを生成する

先ほど定義した`random_walk()`関数を使って、それぞれ 30 ステップの 40 個のランダムウォークを生成します。すべてのランダムウォークを`walks`という名前のリストに格納します。

```python
# Data: 40 random walks as (num_steps, 3) arrays
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
