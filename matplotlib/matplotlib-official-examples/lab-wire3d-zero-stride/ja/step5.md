# 2番目のサブプロットを作成する

`rstride` パラメータを `0` に、`cstride` パラメータを `10` に設定して、2番目のサブプロットを作成します。

```python
ax2.plot_wireframe(X, Y, Z, rstride=0, cstride=10)
ax2.set_title("Row (y) stride set to 0")
```
