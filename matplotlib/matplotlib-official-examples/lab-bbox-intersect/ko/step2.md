# 사각형 설정

`left`, `bottom`, `width`, 및 `height` 변수를 사용하여 사각형의 위치와 치수를 정의합니다. 그런 다음, `Rectangle` 클래스를 사용하여 사각형을 생성하고, `add_patch` 메서드를 사용하여 플롯에 추가합니다.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
