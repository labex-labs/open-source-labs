# 定义参数

在这一步中，我们将定义在鸢尾花数据集上绘制决策面所需的参数。

```python
# 参数
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # 决策面等高线的精细步长
plot_step_coarser = 0.5  # 粗略分类器猜测的步长
RANDOM_SEED = 13  # 在每次迭代时固定种子
```
