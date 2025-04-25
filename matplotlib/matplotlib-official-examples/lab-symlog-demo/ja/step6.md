# x 軸と y 軸の両方に symlog プロットを作成する

3 番目のサブプロットでは、x 軸と y 軸の両方に `symlog` プロットを作成します。また、`linthresh` パラメータを 0.015 に設定します。

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```
