# プロットの向きを変更する

このステップでは、`orientation`パラメータを使ってプロットの向きを変更します。ステムが x 方向に投影され、ベースラインが yz 平面にあるように、向きを`'x'`に設定します。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
