# 散布図の作成

ここでは、`matplotlib.pyplot` の `plot` 関数を使用して散布図を作成します。

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
