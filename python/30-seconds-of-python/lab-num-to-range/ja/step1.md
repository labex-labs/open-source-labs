# 数値を範囲にマッピングする

`num_to_range` という関数を作成します。この関数は、`num`、`inMin`、`inMax`、`outMin`、および `outMax` の5つの引数をとります。この関数は、`inMin` から `inMax` の範囲内にある `num` を、`outMin` から `outMax` の範囲にマッピングした値を返す必要があります。言い換えると、この関数は特定の範囲 (`inMin` から `inMax`) に含まれる数値 (`num`) を取り、新しい範囲 (`outMin` から `outMax`) にマッピングする必要があります。

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
