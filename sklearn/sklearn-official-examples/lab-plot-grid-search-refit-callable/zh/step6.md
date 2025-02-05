# 可视化结果

我们将通过绘制准确率与主成分分析（PCA）组件数量的关系图来可视化结果。

```python
n_components = grid.cv_results_["param_reduce_dim__n_components"]
test_scores = grid.cv_results_["mean_test_score"]

plt.figure()
plt.bar(n_components, test_scores, width=1.3, color="b")

lower = lower_bound(grid.cv_results_)
plt.axhline(np.max(test_scores), linestyle="--", color="y", label="最佳分数")
plt.axhline(lower, linestyle="--", color=".5", label="最佳分数 - 1个标准差")

plt.title("平衡模型复杂度和交叉验证分数")
plt.xlabel("使用的PCA组件数量")
plt.ylabel("数字分类准确率")
plt.xticks(n_components.tolist())
plt.ylim((0, 1.0))
plt.legend(loc="upper left")

best_index_ = grid.best_index_

print("最佳索引是 %d" % best_index_)
print("选择的主成分数量是 %d" % n_components[best_index_])
print(
    "相应的准确率分数是 %.2f"
    % grid.cv_results_["mean_test_score"][best_index_]
)
plt.show()
```
