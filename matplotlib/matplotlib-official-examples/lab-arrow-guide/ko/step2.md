# 표시 공간에서 고정된 머리 모양 및 앵커 포인트

이는 플롯에 주석을 달 때 유용하며, 플롯을 이동하거나 크기를 조정할 때 화살표의 모양이나 위치가 변경되지 않도록 하려는 경우에 적합합니다.

```python
fig, axs = plt.subplots(nrows=2)
arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head),
                                 mutation_scale=100,
                                 transform=axs[0].transAxes)
axs[0].add_patch(arrow)

arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (x_head, y_head),
                                 mutation_scale=100,
                                 transform=axs[1].transAxes)
axs[1].add_patch(arrow)
axs[1].set(xlim=(0, 2), ylim=(0, 2))

plt.show()
```
