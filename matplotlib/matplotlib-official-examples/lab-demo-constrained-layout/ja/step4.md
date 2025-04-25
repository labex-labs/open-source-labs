# 制約付きレイアウトでサブプロットを作成する

同じ 2x2 のサブプロットを作成しますが、今回は「制約付きレイアウト」を使用します。これにより、軸オブジェクトとラベルの間の重複を防ぐために、サブプロットが自動的に調整されます。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
