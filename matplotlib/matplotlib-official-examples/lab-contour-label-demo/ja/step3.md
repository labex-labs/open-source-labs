# 辞書を使って任意の文字列を使って等高線にラベルを付ける

辞書を使って、任意の文字列を使って等高線にラベルを付けることもできます。これにより、カスタムラベルで等高線にラベルを付けることができます。この例では、文字列をリストとして使って等高線にラベルを付けます。

```python
fig1, ax1 = plt.subplots()
CS1 = ax1.contour(X, Y, Z)

fmt = {}
strs = ['first','second', 'third', 'fourth', 'fifth','sixth','seventh']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s

ax1.clabel(CS1, CS1.levels[::2], inline=True, fmt=fmt, fontsize=10)
```
