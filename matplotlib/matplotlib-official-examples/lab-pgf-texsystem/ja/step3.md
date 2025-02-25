# プロットを作成する

これで、`plt.subplots()`関数を使ってプロットを作成できます。この例では、単純な折れ線グラフを作成します。

```python
fig, ax = plt.subplots(figsize=(4.5, 2.5))

ax.plot(range(5))
```
