# 别名

为了在交互模式下减少按键次数，许多属性都有简短的别名，例如，“lw”代表“linewidth”，“mec”代表“markeredgecolor”。在自省模式下调用 `set` 或 `get` 时，这些属性将以“全名”或“别名”列出。

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```
