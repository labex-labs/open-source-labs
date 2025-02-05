# 可视化结果

我们使用柱状图来可视化非嵌套和嵌套交叉验证的结果。

```python
from matplotlib import pyplot as plt

# 绘制差异的柱状图。
plt.bar(["非嵌套", "嵌套"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("分数")
plt.title("非嵌套和嵌套交叉验证分数")
plt.show()
```
