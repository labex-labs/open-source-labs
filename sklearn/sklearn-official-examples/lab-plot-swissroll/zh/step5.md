# 生成瑞士洞数据集

我们通过在 `make_swiss_roll()` 函数中使用 `hole=True` 参数给瑞士卷数据集添加一个洞来生成瑞士洞数据集。

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```
