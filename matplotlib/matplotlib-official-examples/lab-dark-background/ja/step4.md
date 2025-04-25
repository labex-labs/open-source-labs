# データをプロットする

このステップでは、前のステップで生成したサンプルデータをプロットします。異なる位相の複数のサイン波をプロットするために、`for`ループを使用します。

```python
fig, ax = plt.subplots()

ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    # 位相シフト s のサイン波をプロットする
    ax.plot(x, np.sin(x + s), 'o-')

ax.set_xlabel('x 軸')
ax.set_ylabel('y 軸')
ax.set_title("'dark_background' スタイルシート")

plt.show()
```
