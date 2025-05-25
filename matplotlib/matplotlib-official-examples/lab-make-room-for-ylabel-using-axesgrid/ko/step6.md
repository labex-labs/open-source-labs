# 두 개의 조정 가능한 축을 가진 Figure 생성

이 단계에서는 두 개의 조정 가능한 축을 가진 figure 를 생성합니다. `make_axes_locatable` 메서드를 사용하여 축을 조정할 수 있는 divider 를 생성합니다. `append_axes` 메서드를 사용하여 첫 번째 축의 오른쪽에 새로운 축을 추가합니다.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
