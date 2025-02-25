# 目盛りラベルにパディングを追加する

このステップでは、浮動軸上の目盛りラベルにパディングを追加します。これは、`major_ticklabels`オブジェクトの`pad`属性を望ましいパディング値に設定することで行えます。

```python
# Add Padding to Tick Labels
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticklabels.set_pad(10)

plt.show()
```
