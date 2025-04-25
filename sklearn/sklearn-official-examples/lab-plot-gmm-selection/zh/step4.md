# 绘制 BIC 分数

我们根据网格搜索进行的交叉验证结果创建一个`pandas.DataFrame`。我们将 BIC 分数的符号重新取反，以展示最小化它的效果。我们使用`seaborn`来绘制 BIC 分数。

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame(grid_search.cv_results_)[
    ["param_n_components", "param_covariance_type", "mean_test_score"]
]
df["mean_test_score"] = -df["mean_test_score"]
df = df.rename(
    columns={
        "param_n_components": "组件数量",
        "param_covariance_type": "协方差类型",
        "mean_test_score": "BIC 分数"
    }
)
df.sort_values(by="BIC 分数").head()

sns.catplot(
    data=df,
    kind="bar",
    x="组件数量",
    y="BIC 分数",
    hue="协方差类型"
)
plt.show()
```
