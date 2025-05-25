# Constrained Layout 으로 중첩된 Gridspecs 생성

*constrained layout*을 사용하여 중첩된 gridspecs 를 사용하는 더 복잡한 예제를 생성합니다. 이를 통해 서브플롯의 레이아웃을 더 세밀하게 제어할 수 있습니다.

```python
fig = plt.figure(layout='constrained')

gs0 = gridspec.GridSpec(1, 2, figure=fig)

gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
for n in range(3):
    ax = fig.add_subplot(gs1[n])
    example_plot(ax)


gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
for n in range(2):
    ax = fig.add_subplot(gs2[n])
    example_plot(ax)

plt.show()
```
