# x軸にsymlogプロットを作成する

最初のサブプロットでは、x軸に `symlog` プロットを作成します。また、x軸に補助グリッドを追加します。

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
