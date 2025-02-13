# 将数字映射到指定范围

## 问题

编写一个名为 `num_to_range` 的函数，该函数接受五个参数：`num`、`inMin`、`inMax`、`outMin` 和 `outMax`。该函数应返回 `num` 在从 `inMin` 到 `inMax` 的范围内映射到 `outMin` 到 `outMax` 范围内的值。换句话说，该函数应接受一个落在特定范围（`inMin` 到 `inMax`）内的数字（`num`），并将其映射到一个新的范围（`outMin` 到 `outMax`）。

## 示例

```python
num_to_range(5, 0, 10, 0, 100) # 50.0
```

在此示例中，我们将数字 5 从 0 到 10 的范围映射到 0 到 100 的范围。结果应为 50.0。
