# Ticked Patheffect 를 사용하여 직선 플롯

이제 Ticked Patheffect 를 사용하여 대각선 직선을 플롯합니다.

```python
# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])
```
