# 部分依存性プロットを作成して可視化する

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# グラフのサイズとタイトルを設定する
fig.set_size_inches(10, 8)
fig.suptitle('Partial Dependence Plots')

plt.show()
```
