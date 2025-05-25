# Y-축 레이블 자동 정렬

세 번째 단계는 `.Figure.align_ylabels` 메서드를 사용하여 y-축 레이블을 자동으로 정렬하는 것입니다.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)
fig.align_ylabels(axs[:, 1])
plt.show()
```
