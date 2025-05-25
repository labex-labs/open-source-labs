# Y-축 레이블 수동 정렬

네 번째 단계는 y-축 객체의 `~.Axis.set_label_coords` 메서드를 사용하여 y-축 레이블을 수동으로 정렬하는 것입니다.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # axes coords

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```
