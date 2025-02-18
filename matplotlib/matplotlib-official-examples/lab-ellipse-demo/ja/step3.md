# 異なる角度の楕円を描画する

この例では、異なる角度の多数の楕円を描画します。描画したい各角度に対して `Ellipse` インスタンスを作成するためにループを使用します。

```python
# 角度のステップと描画する角度の範囲を定義する
angle_step = 45  # 度
angles = np.arange(0, 180, angle_step)

# プロットを作成し、アスペクト比を 'equal' に設定する
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# 角度をループし、各角度に対して楕円を描画する
for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

# プロットの x 軸と y 軸の範囲を設定する
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# プロットを表示する
plt.show()
```
