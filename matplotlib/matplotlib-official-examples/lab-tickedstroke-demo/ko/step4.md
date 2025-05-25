# 눈금의 방향/측면

이 단계에서는 눈금의 측면을 변경합니다.

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

이 코드는 양쪽에 눈금이 있는 선을 생성합니다.
