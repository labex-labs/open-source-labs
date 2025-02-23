# 調整可能なデータ制限付きの対数対数プロットの作成

次に、調整可能なデータ制限付きの対数対数プロットを作成します。これは、x 軸と y 軸の両方が対数スケールになり、プロットのアスペクト比がデータに合うように調整されることを意味します。

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```
