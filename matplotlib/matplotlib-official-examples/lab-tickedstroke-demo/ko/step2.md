# 선에 TickedStroke 적용하기

이 단계에서는 선에 TickedStroke 를 적용합니다.

```python
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```

이 코드는 TickedStroke path effect 를 가진 선과 곡선을 생성합니다.
