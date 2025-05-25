# 다각형 근사 (Polygonal Approximation) 를 사용하여 타원 플롯 (Plot)

이 단계에서는 다각형 근사를 사용하여 타원을 플롯합니다.

```python
ax = fig.add_subplot(212, aspect='equal')
ax.fill(x, y, alpha=0.2, facecolor='green', edgecolor='green', zorder=1)
e2 = patches.Arc((xcenter, ycenter), width, height,
                 angle=angle, linewidth=2, fill=False, zorder=2)

ax.add_patch(e2)
fig.savefig('arc_compare')

plt.show()
```
