# 個別条件期待値プロットを作成して可視化する

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# グラフのサイズとタイトルを設定する
fig.set_size_inches(10, 8)
fig.suptitle('Individual Conditional Expectation Plots')

plt.show()
```
