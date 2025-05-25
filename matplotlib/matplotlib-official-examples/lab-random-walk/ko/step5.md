# 3D 플롯 생성

`matplotlib`을 사용하여 3D 플롯을 생성합니다. 각 랜덤 워크에 대해 빈 선을 플롯에 추가합니다. x, y, z 축의 범위를 0 과 1 사이로 설정합니다.

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
