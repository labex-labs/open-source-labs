# 상호 작용성 추가

산점도에서 점을 클릭하면 해당 점을 생성한 데이터 세트의 원시 데이터를 플롯하려고 합니다. 점이 클릭될 때 호출될 함수 `onpick`을 정의합니다. 이 함수는 원시 데이터를 플롯하고 해당 데이터 세트의 평균과 표준 편차를 표시합니다.

```python
def onpick(event):

    if event.artist != line:
        return

    N = len(event.ind)
    if not N:
        return

    figi, axs = plt.subplots(N, squeeze=False)
    for ax, dataind in zip(axs.flat, event.ind):
        ax.plot(X[dataind])
        ax.text(.05, .9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                transform=ax.transAxes, va='top')
        ax.set_ylim(-0.5, 1.5)
    figi.show()


fig.canvas.mpl_connect('pick_event', onpick)
```
