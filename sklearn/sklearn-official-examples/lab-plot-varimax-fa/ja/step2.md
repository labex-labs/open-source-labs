# バリマックス回転を用いた因子分析を実行する

ここでは、バリマックス回転を用いてアイリスデータセットに対して因子分析を実行し、データの根底にある構造を明らかにします。結果を主成分分析（PCA）と回転なしの因子分析と比較します。

```python
# バリマックス回転を用いた因子分析を実行する
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("回転なしのFA", FactorAnalysis()),
    ("バリマックスFA", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(methods), figsize=(10, 8), sharey=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    components = fa.components_.T
    print("\n\n %s :\n" % method)
    print(components)

    vmax = np.abs(components).max()
    ax.imshow(components, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_yticklabels(feature_names)
    ax.set_title(str(method))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Comp. 1", "Comp. 2"])
fig.suptitle("因子")
plt.tight_layout()
plt.show()
```
