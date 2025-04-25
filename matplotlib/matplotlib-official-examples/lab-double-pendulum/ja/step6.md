# グラフを設定する

次に、シミュレーション用のグラフを設定します。振り子の最大長に等しい x と y の範囲を持つグラフを作成し、アスペクト比を等しく設定し、グリッドを追加します。

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
