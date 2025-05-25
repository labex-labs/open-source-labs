# 두 개의 교차하는 선을 그리고 위에 정의된 `AngleAnnotation` 도구를 사용하여 각 각도에 레이블을 지정합니다.

```python
fig, ax = plt.subplots()
fig.canvas.draw()  # 렌더러를 정의하려면 그림을 그려야 합니다.
ax.set_title("AngleLabel 예시")

# 두 개의 교차하는 선을 그리고 위에 정의된
# ``AngleAnnotation`` 도구를 사용하여 각 각도에 레이블을 지정합니다.
center = (4.5, 650)
p1 = [(2.5, 710), (6.0, 605)]
p2 = [(3.0, 275), (5.5, 900)]
line1, = ax.plot(*zip(*p1))
line2, = ax.plot(*zip(*p2))
point, = ax.plot(*center, marker="o")

am1 = AngleAnnotation(center, p1[1], p2[1], ax=ax, size=75, text=r"$\alpha$")
am2 = AngleAnnotation(center, p2[1], p1[0], ax=ax, size=35, text=r"$\beta$")
am3 = AngleAnnotation(center, p1[0], p2[0], ax=ax, size=75, text=r"$\gamma$")
am4 = AngleAnnotation(center, p2[0], p1[1], ax=ax, size=35, text=r"$\theta$")


# 각도 호와 텍스트에 대한 몇 가지 스타일 옵션을 보여줍니다.
p = [(6.0, 400), (5.3, 410), (5.6, 300)]
ax.plot(*zip(*p))
am5 = AngleAnnotation(p[1], p[0], p[2], ax=ax, size=40, text=r"$\Phi$",
                      linestyle="--", color="gray", textposition="outside",
                      text_kw=dict(fontsize=16, color="gray"))

plt.show()
```
