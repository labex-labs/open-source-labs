# 生成随机游走

我们使用之前定义的 `random_walk()` 函数生成 40 个随机游走，每个随机游走有 30 步。我们将所有的随机游走存储在一个名为 `walks` 的列表中。

```python
# 数据：40 个随机游走，形式为 (num_steps, 3) 数组
num_steps = 30
walks = [random_walk(num_steps) for index in range(40)]
```
