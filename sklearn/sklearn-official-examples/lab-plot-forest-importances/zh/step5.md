# 基于特征排列的特征重要性

排列特征重要性克服了基于杂质的特征重要性的局限性：它们对高基数特征没有偏差，并且可以在留出的测试集上计算。我们将计算完整的排列重要性。特征被随机打乱 n 次，并且重新拟合模型以估计其重要性。我们将绘制重要性排名。

```python
start_time = time.time()
result = permutation_importance(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(result.importances_mean, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.show()
```
