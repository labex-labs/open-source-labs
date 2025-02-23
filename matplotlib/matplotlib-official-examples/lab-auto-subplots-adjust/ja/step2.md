# グラフを作成する

長いy軸のラベル付きの単純な折れ線グラフを作成しましょう。

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
