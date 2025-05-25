# 리커 웨이블릿 함수 정의

리커 웨이블릿과 리커 웨이블릿 사전을 생성하는 함수를 정의합니다.

```python
def ricker_function(resolution, center, width):
    """이산적으로 서브샘플링된 리커 (멕시칸 해트) 웨이블릿"""
    x = np.linspace(0, resolution - 1, resolution)
    x = (
        (2 / (np.sqrt(3 * width) * np.pi**0.25))
        * (1 - (x - center) ** 2 / width**2)
        * np.exp(-((x - center) ** 2) / (2 * width**2))
    )
    return x


def ricker_matrix(width, resolution, n_components):
    """리커 (멕시칸 해트) 웨이블릿 사전"""
    centers = np.linspace(0, resolution - 1, n_components)
    D = np.empty((n_components, resolution))
    for i, center in enumerate(centers):
        D[i] = ricker_function(resolution, center, width)
    D /= np.sqrt(np.sum(D**2, axis=1))[:, np.newaxis]
    return D
```
