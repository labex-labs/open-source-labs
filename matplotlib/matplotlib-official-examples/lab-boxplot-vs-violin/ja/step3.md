# バイオリンプロットの作成

`violinplot()` メソッドを使ってバイオリンプロットを作成します。このメソッドは、データ、平均値の表示、中央値の表示など、複数の引数をとります。

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
