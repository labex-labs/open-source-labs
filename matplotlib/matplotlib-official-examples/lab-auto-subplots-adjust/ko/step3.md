# draw 콜백 함수 정의

그래프가 그려질 때마다 호출될 함수를 정의합니다. 이 함수는 y-레이블의 경계 상자 (bounding box) 를 계산하고, 서브플롯이 레이블을 위한 충분한 공간을 남겨두는지 확인하며, 필요한 경우 서브플롯 매개변수를 조정합니다.

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # Bounding box in pixels
        bbox_px = label.get_window_extent()
        # Transform to relative figure coordinates. This is the inverse of
        # transFigure.
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # the bbox that bounds all the bboxes, again in relative figure coords
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # Move the subplot left edge more to the right
        fig.subplots_adjust(left=1.1*bbox.width)  # pad a little
        fig.canvas.draw()
```
