# 横型のカラーバー付きのプロットを作成する

次に、横型のカラーバー付きのプロットを作成します。ステップ2と同じ手順をたどりますが、今回は `afmhot` カラーマップを使い、カラーバーの方向を横に設定します。

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
