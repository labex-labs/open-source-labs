# 산점도에서 선택

산점도는 `~matplotlib.collections.PathCollection`에 의해 지원됩니다. 산점도를 생성하고 선택을 활성화합니다.

```python
x, y, c, s = rand(4, 100)


def onpick3(event):
    ind = event.ind
    print('onpick3 scatter:', ind, x[ind], y[ind])


fig, ax = plt.subplots()
ax.scatter(x, y, 100*s, c, picker=True)
fig.canvas.mpl_connect('pick_event', onpick3)
```
