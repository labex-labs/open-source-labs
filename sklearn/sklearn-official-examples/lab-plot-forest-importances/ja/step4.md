# 不純度の平均減少量に基づく特徴量の重要度

特徴量の重要度は、適合させた属性`feature_importances_`によって提供され、各木内の不純度の減少の累積の平均と標準偏差として計算されます。不純度に基づく重要度をプロットします。

```python
start_time = time.time()
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
```
