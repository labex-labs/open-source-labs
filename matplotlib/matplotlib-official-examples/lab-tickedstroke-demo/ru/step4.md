# Направление/сторона тиков

В этом шаге мы изменим сторону тиков.

```python
fig, ax = plt.subplots(figsize=(6, 6))
line_x = line_y = [0, 1]
ax.plot(line_x, line_y, label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

ax.plot(line_x, line_y, label="Opposite side",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=-135)])

ax.legend()
plt.show()
```

Этот код создаст линию с тиками с обеих сторон.
