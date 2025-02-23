# y 軸のラベルを自動的に整列させる

3 番目のステップは、`.Figure.align_ylabels` メソッドを使って y 軸のラベルを自動的に整列させることです。

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```
