# 四角形の作成

`matplotlib.patches` モジュールの `Rectangle()` 関数を使って、グラフに四角形を作成します。四角形を作成した後、`set_xlim()` と `set_ylim()` 関数を使って、その水平および垂直の範囲を設定します。最後に、四角形をグラフに追加します。

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# 軸座標に四角形を作成する
left, width =.25,.5
bottom, height =.25,.5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# 水平および垂直の範囲を設定する
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
