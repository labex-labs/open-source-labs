# Ticked Patheffect 를 사용하여 곡선 플롯

이제 Ticked Patheffect 를 사용하여 곡선 라인을 플롯합니다.

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
