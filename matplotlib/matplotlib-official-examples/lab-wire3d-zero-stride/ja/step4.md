# 最初のサブプロットを作成する

最初のサブプロットを作成します。このとき、`rstride` パラメータを `10` に、`cstride` パラメータを `0` に設定します。

```python
ax1.plot_wireframe(X, Y, Z, rstride=10, cstride=0)
ax1.set_title("Column (x) stride set to 0")
```
