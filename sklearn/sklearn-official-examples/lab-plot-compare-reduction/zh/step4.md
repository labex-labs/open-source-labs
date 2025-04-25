# 绘制结果

我们将使用柱状图来绘制`GridSearchCV`的结果。这将使我们能够比较不同特征约简技术的准确性。

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# 分数按照 param_grid 迭代顺序排列，即字母顺序
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# 选择最佳 C 的分数
mean_scores = mean_scores.max(axis=0)
# 创建一个数据框以方便绘图
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("Comparing feature reduction techniques")
ax.set_xlabel("Reduced number of features")
ax.set_ylabel("Digit classification accuracy")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```
