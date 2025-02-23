# サンプルのy=xグラフにおける「symlog」と「asinh」の挙動を比較する

サンプルのy=xグラフにおける「symlog」と「asinh」の挙動を比較します。同じグラフを2回プロットします。1回は「symlog」で、もう1回は「asinh」でプロットします。

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
