# プロットのカスタマイズ

グリッドの色を変更し、凡例を追加することで、プロットをカスタマイズできます。この例では、凡例をプロットの中心から少し離して、重なりを避けます。

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2,.5 + np.sin(angle)/2))
```
