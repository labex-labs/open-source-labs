# y 軸のラベルを手動で整列させる

4 番目のステップは、y 軸オブジェクトの `~.Axis.set_label_coords` メソッドを使って y 軸のラベルを手動で整列させることです。

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```
