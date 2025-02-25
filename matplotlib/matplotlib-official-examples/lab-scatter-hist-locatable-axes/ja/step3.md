# 散布図を作成する

このステップでは、ステップ2のランダムなデータを使って散布図を作成します。

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
