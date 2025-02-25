# グラフの壁に等高線プロファイルを投影する

このステップでは、各次元の等高線を適切なオフセットで描画することにより、グラフの壁に等高線プロファイルを投影します。

```python
# Plot projections of the contours for each dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
