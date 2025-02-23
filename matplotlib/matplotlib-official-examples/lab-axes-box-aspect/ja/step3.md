# 正方形の双子の軸

親のボックスアスペクトを引き継ぐ双子の軸を持つ正方形の軸を作成します。

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```
