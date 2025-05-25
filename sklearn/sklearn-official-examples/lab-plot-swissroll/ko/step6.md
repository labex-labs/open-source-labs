# 스위스 홀 데이터셋 시각화

생성된 스위스 홀 데이터셋을 3 차원 산점도로 시각화하여 서로 다른 점을 나타낼 수 있습니다.

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(sh_points[:, 0], sh_points[:, 1], sh_points[:, 2], c=sh_color, s=50, alpha=0.8)
ax.set_title("스위스 홀 (Ambient Space)")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
```
