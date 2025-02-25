# データをプロットする

`plot_wireframe`を使って、3つのサブプロットのそれぞれにデータをプロットします。

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
