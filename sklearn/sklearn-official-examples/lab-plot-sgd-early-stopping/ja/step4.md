# 結果をプロットする

最後のステップは、結果をプロットすることです。学習とテストのスコア、および反復回数と学習時間をプロットするために 2 つのサブプロットを使用します。各推定器と停止基準に対して異なる線のスタイルを使用します。

```python
# プロットする内容を定義する
lines = "停止基準"
x軸 = "max_iter"
スタイル = ["-.", "--", "-"]

# 最初のプロット：学習とテストのスコア
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y軸 in zip(axes, ["学習スコア", "テストスコア"]):
    for スタイル, (基準, group_df) in zip(スタイル, results_df.groupby(lines)):
        group_df.plot(x=x軸, y=y軸, label=基準, ax=ax, style=スタイル)
    ax.set_title(y軸)
    ax.legend(title=lines)
fig.tight_layout()

# 2 番目のプロット：n_iter と学習時間
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y軸 in zip(axes, ["n_iter_", "学習時間 (秒)"]):
    for スタイル, (基準, group_df) in zip(スタイル, results_df.groupby(lines)):
        group_df.plot(x=x軸, y=y軸, label=基準, ax=ax, style=スタイル)
    ax.set_title(y軸)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
