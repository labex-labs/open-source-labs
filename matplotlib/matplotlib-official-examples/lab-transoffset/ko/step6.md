# 극좌표 플롯에 텍스트 추가

마지막으로, `offset_copy`와 `matplotlib.pyplot`의 `text` 함수를 사용하여 극좌표 플롯에 텍스트를 추가합니다.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       y=6, units='dots')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)),
             transform=trans_offset,
             horizontalalignment='center',
             verticalalignment='bottom')
```
