# 创建一个带有水平颜色条的绘图

现在我们将创建一个带有水平颜色条的绘图。我们将遵循与步骤 2 相同的步骤，但这次我们将使用 `afmhot` 颜色映射，并将颜色条的方向设置为水平。

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
