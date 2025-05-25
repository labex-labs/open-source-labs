# 등고선 플롯 생성

이제 `ax.contour()` 메서드를 사용하여 등고선 플롯을 생성합니다. 이 메서드는 목적 함수의 지형을 표현하고 제약 조건 함수의 경계 곡선을 생성하는 데 사용됩니다.

```python
fig, ax = plt.subplots(figsize=(6, 6))

cntr = ax.contour(x1, x2, obj, [0.01, 0.1, 0.5, 1, 2, 4, 8, 16], colors='black')
ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)

cg1 = ax.contour(x1, x2, g1, [0], colors='sandybrown')
plt.setp(cg1.collections, path_effects=[patheffects.withTickedStroke(angle=135)])

cg2 = ax.contour(x1, x2, g2, [0], colors='orangered')
plt.setp(cg2.collections, path_effects=[patheffects.withTickedStroke(angle=60, length=2)])

cg3 = ax.contour(x1, x2, g3, [0], colors='mediumblue')
plt.setp(cg3.collections, path_effects=[patheffects.withTickedStroke(spacing=7)])

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

plt.show()
```
