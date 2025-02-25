# 三角分割を作成する

`matplotlib.tri.Triangulation` を使って三角分割を作成します。三角形を指定する必要はありませんので、点のデレニー三角分割が自動的に作成されます。

```python
triang = tri.Triangulation(x, y)
```
