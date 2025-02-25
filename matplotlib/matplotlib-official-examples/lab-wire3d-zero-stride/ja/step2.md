# グラフと2つのサブプロットを作成する

`subplots()` メソッドを使って、2つのサブプロット付きのグラフを作成します。また、サブプロットを3次元にするために、投影を `'3d'` に設定します。

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
