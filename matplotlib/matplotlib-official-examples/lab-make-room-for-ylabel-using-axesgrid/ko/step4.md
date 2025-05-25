# 두 개의 축을 가진 Figure 생성

이 단계에서는 두 개의 축을 가진 figure 를 생성합니다. `add_axes` 메서드를 사용하여 figure 에 두 개의 축을 추가합니다. 또한 첫 번째 축에 대한 y-tick 레이블과 두 번째 축에 대한 제목을 설정합니다.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
