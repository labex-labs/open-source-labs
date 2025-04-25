# y 軸に symlog プロットを作成する

2 番目のサブプロットでは、y 軸に `symlog` プロットを作成します。

```python
ax1.plot(y1, x)
ax1.set_yscale('symlog')
ax1.set_ylabel('symlogy')
```
