# 하이퍼링크가 있는 이미지 생성

이 단계에서는 이미지를 생성하고 하이퍼링크를 추가합니다. 이미지를 생성하는 코드는 다음과 같습니다.

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

이미지에 하이퍼링크를 추가하려면 이미지 객체의 `set_url()` 메서드를 사용해야 합니다. 이 메서드는 URL 을 인수로 받습니다. 업데이트된 코드는 다음과 같습니다.

```python
im.set_url('https://www.google.com/')
```

이미지는 `https://www.google.com/`에 대한 하이퍼링크를 갖습니다. 마지막으로, `fig.savefig()`를 사용하여 플롯을 SVG 파일로 저장할 수 있습니다.

```python
fig.savefig('image.svg')
```
