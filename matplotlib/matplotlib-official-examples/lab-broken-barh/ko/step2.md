# 끊어진 수평 막대 그래프 만들기

이 단계에서는 끊어진 수평 막대 그래프를 만듭니다. `Axes` 클래스의 `broken_barh()` 메서드를 사용하여 그래프를 생성합니다. `broken_barh()` 메서드는 세 개의 인수를 받습니다. 첫 번째 인수는 각 튜플이 막대의 세그먼트를 나타내는 튜플 목록이며, 튜플의 첫 번째 요소는 세그먼트의 시작점이고 두 번째 요소는 세그먼트의 길이입니다. 두 번째 인수는 막대의 y 좌표이고, 세 번째 인수는 막대의 면 색상입니다.

```python
fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_ylim(5, 35)
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
ax.grid(True)
ax.annotate('race interrupted', (61, 25),
            xytext=(0.8, 0.9), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')

plt.show()
```
