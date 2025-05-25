# Lorenz 함수 정의

세 개의 매개변수를 받아 세 개의 값을 반환하는 Lorenz 함수를 정의합니다. Lorenz 매개변수에 대해 기본값 `s=10`, `r=28`, `b=2.667`을 사용합니다.

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       세 차원 공간의 관심 지점.
    s, r, b : float
       Lorenz 어트랙터 (attractor) 를 정의하는 매개변수.

    Returns
    -------
    xyz_dot : array, shape (3,)
       *xyz*에서 Lorenz 어트랙터의 편미분 값.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
