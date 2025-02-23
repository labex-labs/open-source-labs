# 調整可能なボックス付きの対数対数プロットの作成

次に、調整可能なボックス付きの対数対数プロットを作成します。これは、x 軸と y 軸の両方が対数スケールになり、プロットのアスペクト比が 1 に等しくなることを意味します。

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```
