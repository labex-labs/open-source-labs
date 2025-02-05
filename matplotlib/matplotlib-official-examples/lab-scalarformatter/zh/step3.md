# 为示例图表创建子图

我们将创建一个 3x3 的子图网格来展示我们的示例图表。

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
