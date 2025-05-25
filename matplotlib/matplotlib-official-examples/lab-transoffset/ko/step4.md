# 산점도에 텍스트 추가

이제 `offset_copy`를 사용하여 산점도에 텍스트를 추가합니다. 먼저, 임의의 좌표계에서 주어진 위치를 기준으로 화면 좌표에서 지정된 오프셋에 텍스트를 배치하는 변환 (transform) 을 생성합니다. 그런 다음, `matplotlib.pyplot`의 `text` 함수를 사용하여 플롯에 텍스트를 추가합니다.

```python
# Create the transform
trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=0.05, y=0.10, units='inches')

# Add text to the plot
for x, y in zip(xs, ys):
    plt.text(x, y, '%d, %d' % (int(x), int(y)), transform=trans_offset)
```
