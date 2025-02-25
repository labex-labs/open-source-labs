# グラフとサブプロットを作成する

データをプロットするために、グラフとサブプロットを作成する必要があります。2つのサブプロットを持つプロットを作成します。

```python
fig = plt.figure()

ax = fig.add_subplot(211)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")

ax = fig.add_subplot(223)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")
```
