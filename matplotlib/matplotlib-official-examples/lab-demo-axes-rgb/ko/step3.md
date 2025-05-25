# RGB 큐브 생성 함수 정의

이 단계에서는 이전 단계에서 얻은 R, G, B 채널로부터 RGB 큐브를 생성하는 `make_cube()` 함수를 정의합니다. 이 함수는 R, G, B 큐브와 RGB 이미지를 반환합니다.

```python
def make_cube(r, g, b):
    # Get the shape of R
    ny, nx = r.shape

    # Create the R, G, and B cubes
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Combine the R, G, and B cubes to create the RGB image
    RGB = R + G + B

    return R, G, B, RGB
```
