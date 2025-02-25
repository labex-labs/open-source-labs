# グラフの作成

このステップでは、先ほど生成したランダムなデータを使ってグラフを作成します。具体的には、各データポイントをマーカーとしてプロットします。成功変数によって決まる成功シンボル、技術変数によって決まるサイズ、離陸角度変数によって決まる回転、推力変数によって決まる色を持たせます。

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```
