# ラベルと Z 目盛りを設定する

`set` メソッドを使ってラベルと Z 目盛りを設定します。X、Y、Z 座標のラベルを設定し、ボックスの深さを示すように Z 目盛りを設定します。

```python
# Set labels and zticks
ax.set(
    xlabel='X [km]',
    ylabel='Y [km]',
    zlabel='Z [m]',
    zticks=[0, -150, -300, -450],
)
```
