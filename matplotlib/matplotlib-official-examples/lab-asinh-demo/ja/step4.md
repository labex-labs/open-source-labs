# サンプルの y=x グラフにおける「symlog」と「asinh」の挙動を比較する

サンプルの y=x グラフにおける「symlog」と「asinh」の挙動を比較します。同じグラフを 2 回プロットします。1 回は「symlog」で、もう 1 回は「asinh」でプロットします。

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
