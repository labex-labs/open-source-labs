# 加重平均

同じ長さの2つのリスト：`nums` と `weights` を引数とする関数 `weighted_average(nums, weights)` を書きます。この関数は、`nums` の数値の加重平均を返す必要があります。ここで、各数値は `weights` 内の対応する重みで乗算されます。加重平均は、各数値とその重みの積の和を重みの和で割ることによって計算されます。

```python
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```
