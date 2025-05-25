# 눈금 레이블에 패딩 추가

이 단계에서는 부동 축의 눈금 레이블에 패딩을 추가합니다. 이는 `major_ticklabels` 객체의 `pad` 속성을 원하는 패딩 값으로 설정하여 수행할 수 있습니다.

```python
# Add Padding to Tick Labels
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticklabels.set_pad(10)

plt.show()
```
