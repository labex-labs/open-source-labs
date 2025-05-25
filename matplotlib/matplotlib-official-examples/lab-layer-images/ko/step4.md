# 두 번째 이미지 생성

`func3` 함수와 `imshow` 함수를 사용하여 두 번째 이미지를 생성합니다.

```python
Z2 = func3(X, Y)
im2 = plt.imshow(Z2, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear',
                 extent=extent)
```
