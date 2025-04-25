# 制約付きレイアウトなしでサブプロットを作成する

「制約付きレイアウト」を使用せずに、2x2 のサブプロットを持つ図を作成します。これにより、軸上のラベルが重なることになります。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
