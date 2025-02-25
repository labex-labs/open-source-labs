# プロットを作成する

このステップでは、`plot_beta_hist()` 関数を呼び出してパラメータを渡すことでプロットを作成します。

```python
fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")

plt.show()
```
