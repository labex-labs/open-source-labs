# 사용자 정의 히트 테스트 함수 생성

이 단계에서는 picker 를 호출 가능한 함수로 설정하여 사용자 정의 선택기를 정의합니다. 이 함수는 아티스트가 마우스 이벤트에 의해 히트되었는지 여부를 결정합니다. 마우스 이벤트가 아티스트 위에 있으면 hit=True 를 반환하고 props 는 `.PickEvent` 속성에 추가하려는 속성의 딕셔너리입니다.

```python
def line_picker(line, mouseevent):
    """
    Find the points within a certain distance from the mouseclick in
    data coords and attach some extra attributes, pickx and picky
    which are the data points that were picked.
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt(
        (xdata - mouseevent.xdata)**2 + (ydata - mouseevent.ydata)**2)

    ind, = np.nonzero(d <= maxd)
    if len(ind):
        pickx = xdata[ind]
        picky = ydata[ind]
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()


def onpick2(event):
    print('onpick2 line:', event.pickx, event.picky)


fig, ax = plt.subplots()
ax.set_title('custom picker for line data')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)
```
