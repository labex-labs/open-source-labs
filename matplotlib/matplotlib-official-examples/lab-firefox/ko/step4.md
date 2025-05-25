# 플롯 생성

이제 Matplotlib 을 사용하여 플롯을 생성합니다. 두 개의 `PathPatch` 객체를 플롯에 추가합니다. 하나는 주황색으로 채워진 모양이고, 다른 하나는 흰색 윤곽선입니다.

```python
# Set the plot limits
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Create the plot
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # gray background
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # centering
                  ylim=(ymax, ymin),  # centering, upside down
                  xticks=[], yticks=[])  # no ticks

# Add the white outline
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Add the orange shape
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Display the plot
plt.show()
```
