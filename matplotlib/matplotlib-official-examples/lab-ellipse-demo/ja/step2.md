# 個別の楕円を描画する

この例では、ランダムなサイズ、位置、色の多数の楕円を描画します。各楕円は `Ellipse` クラスのインスタンスになります。

```python
# 再現性のために乱数のシードを固定する
np.random.seed(19680801)

# 描画する楕円の数
NUM = 250

# 楕円を生成する
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# プロットを作成し、アスペクト比を 'equal' に設定する
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# 各楕円をプロットに追加する
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# プロットの x 軸と y 軸の範囲を設定する
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# プロットを表示する
plt.show()
```
