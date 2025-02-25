# ホスト軸を作成する

このステップでは、ホスト軸を作成してグリッドヘルパーを設定します。ホスト軸を作成するには、`fig.add_subplot()` を使用します。

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
