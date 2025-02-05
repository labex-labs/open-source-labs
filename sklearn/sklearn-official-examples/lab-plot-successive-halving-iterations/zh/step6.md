# 分析结果

搜索对象的 `cv_results_` 属性包含搜索结果。使用以下代码将其转换为 pandas 数据框：

```python
results = pd.DataFrame(rsh.cv_results_)
```

通过将 `params` 列转换为字符串来创建 `params_str` 列。删除具有相同 `params_str` 和 `iter` 值的重复行：

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

然后，使用 `pivot` 方法根据迭代次数和参数组合对平均测试分数进行透视：

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

最后，使用以下代码绘制迭代过程中的平均测试分数：

```python
ax = mean_scores.plot(legend=False, alpha=0.6)

labels = [
    f"iter={i}\nn_samples={rsh.n_resources_[i]}\nn_candidates={rsh.n_candidates_[i]}"
    for i in range(rsh.n_iterations_)
]

ax.set_xticks(range(rsh.n_iterations_))
ax.set_xticklabels(labels, rotation=45, multialignment="left")
ax.set_title("Scores of candidates over iterations")
ax.set_ylabel("mean test score", fontsize=15)
ax.set_xlabel("iterations", fontsize=15)
plt.tight_layout()
plt.show()
```
