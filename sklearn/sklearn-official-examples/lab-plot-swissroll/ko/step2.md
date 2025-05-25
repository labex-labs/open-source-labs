# 스위스 롤 데이터셋 시각화

다양한 색상으로 서로 다른 점을 표현하는 3 차원 산점도를 사용하여 생성된 스위스 롤 데이터셋을 시각화할 수 있습니다.

```python
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
fig.add_axes(ax)
ax.scatter(sr_points[:, 0], sr_points[:, 1], sr_points[:, 2], c=sr_color, s=50, alpha=0.8)
ax.set_title("스위스 롤 (원래 공간)")
ax.view_init(azim=-66, elev=12)
_ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
```
