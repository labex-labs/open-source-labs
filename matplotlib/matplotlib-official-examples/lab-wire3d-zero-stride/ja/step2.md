# グラフと 2 つのサブプロットを作成する

`subplots()` メソッドを使って、2 つのサブプロット付きのグラフを作成します。また、サブプロットを 3 次元にするために、投影を `'3d'` に設定します。

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
