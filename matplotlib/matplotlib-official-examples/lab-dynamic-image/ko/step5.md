# 애니메이션 프레임 생성

이제 애니메이션의 프레임을 생성할 것입니다. `for` 루프를 사용하여 60 개의 프레임을 생성할 것입니다. 루프의 각 반복에서 x 와 y 데이터를 업데이트한 다음, `imshow` 메서드를 사용하여 새로운 이미지 객체를 생성합니다. 그런 다음 이미지 객체를 `ims` 리스트에 추가합니다.

```python
ims = []
for i in range(60):
    x += np.pi / 15
    y += np.pi / 30
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])
```
