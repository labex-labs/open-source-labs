# 3Dプロットを作成する

`matplotlib`を使って3Dプロットを作成します。各ランダムウォークに対して空の線をプロットに追加します。x軸、y軸、z軸の範囲を0から1の間に設定します。

```python
# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```
