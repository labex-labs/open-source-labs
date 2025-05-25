# extent 정의 및 첫 번째 이미지 생성

extent 를 정의하고 `imshow` 함수를 사용하여 첫 번째 이미지를 생성합니다.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # chessboard
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```
