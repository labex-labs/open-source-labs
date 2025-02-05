# 将数字映射到指定范围

编写一个名为 `num_to_range` 的函数，该函数接受五个参数：`num`、`inMin`、`inMax`、`outMin` 和 `outMax`。该函数应返回 `num` 在从 `inMin` 到 `inMax` 的范围内映射到 `outMin` 到 `outMax` 范围内的值。换句话说，该函数应接受一个落在特定范围（`inMin` 到 `inMax`）内的数字（`num`），并将其映射到一个新的范围（`outMin` 到 `outMax`）。

```python
def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))
```

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```
