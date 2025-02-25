# サブプロット付きのグラフを作成する

`plt.subplots`を使って、3つのサブプロット付きのグラフを作成します。

```python
fig, axs = plt.subplots(1, 3, subplot_kw={'projection': '3d'})
```
