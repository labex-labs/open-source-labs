# 结果可视化

我们可以使用 plotly.express 来可视化超参数调整的结果。我们使用散点图来可视化评分时间和平均测试分数之间的权衡。我们还可以使用平行坐标图来进一步可视化平均测试分数作为调整后的超参数的函数。

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Remove components' prefixes in param_name."""
    if "__" in param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "CV 评分时间 (秒)",
    "mean_test_score": "CV 分数 (准确率)",
}
fig = px.scatter(
    cv_results,
    x="mean_score_time",
    y="mean_test_score",
    error_x="std_score_time",
    error_y="std_test_score",
    hover_data=param_names,
    labels=labels,
)

fig.update_layout(
    title={
        "text": "评分时间与平均测试分数之间的权衡",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# 对 alpha 使用对数刻度
transform_funcs["alpha"] = math.log10
# L1 范数映射到索引 1，L2 范数映射到索引 2
transform_funcs["norm"] = lambda x: 2 if x == "l2" else 1
# 一元语法映射到索引 1，二元语法映射到索引 2
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "文本分类器管道的平行坐标图",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```
