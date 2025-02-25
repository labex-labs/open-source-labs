# グラフとサブプロットの作成

2 つのサブプロット付きのグラフを作成します。最初のサブプロットは 3D サーフェスプロットで、2 番目のサブプロットは 3D ワイヤーフレームプロットになります。

```python
# Create a figure with two subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Add the first subplot with 3D projection
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Add the second subplot with 3D projection
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```
