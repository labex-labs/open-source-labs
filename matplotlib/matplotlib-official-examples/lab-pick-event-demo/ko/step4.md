# 이미지 선택

`.Axes.imshow`를 사용하여 플롯된 이미지는 `~matplotlib.image.AxesImage` 객체입니다. 여러 이미지가 있는 그림을 생성하고 선택을 활성화합니다.

```python
fig, ax = plt.subplots()
ax.imshow(rand(10, 5), extent=(1, 2, 1, 2), picker=True)
ax.imshow(rand(5, 10), extent=(3, 4, 1, 2), picker=True)
ax.imshow(rand(20, 25), extent=(1, 2, 3, 4), picker=True)
ax.imshow(rand(30, 12), extent=(3, 4, 3, 4), picker=True)
ax.set(xlim=(0, 5), ylim=(0, 5))


def onpick4(event):
    artist = event.artist
    if isinstance(artist, AxesImage):
        im = artist
        A = im.get_array()
        print('onpick4 image', A.shape)


fig.canvas.mpl_connect('pick_event', onpick4)
```
