# ハッチ付きの棒グラフを作成する

データがあるので、ハッチ付きの棒グラフを作成できます。ハッチを使って、グラフの棒にパターンを作成できます。この場合、棒にハッチを追加するために hatch パラメータを使用します。

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```
