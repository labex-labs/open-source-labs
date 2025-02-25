# グラフを作成する

次に、`plt.figure()` 関数を使用してグラフを作成する必要があります。サブプロットがグラフ内に収まるようにするため、`layout` パラメータを "constrained" に設定できます。

```python
fig = plt.figure(layout="constrained")
```
