# プロットを生成する

このステップでは、`scatter()` 関数の入力として `data` 辞書を使用して散布図を生成します。`a`、`b`、`c`、および `d` 変数に対応する文字列を使用してプロットを生成します。

```python
fig, ax = plt.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
plt.show()
```
