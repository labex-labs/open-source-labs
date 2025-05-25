# 삼각형 꼭지점으로부터의 거리에 따른 등고선

이 단계에서는 삼각형 꼭지점으로부터의 거리에 따라 등고선을 그립니다. 개별 점으로부터의 거리에 대한 함수를 정의하고 이 함수에 따라 등고선을 그립니다.

```python
# Define a nice function of distance from individual pts
def f(x, y, pts):
    z = np.zeros_like(x)
    for p in pts:
        z = z + 1/(np.sqrt((x - p[0])**2 + (y - p[1])**2))
    return 1/z

X, Y = np.meshgrid(np.linspace(-1, 1, 51), np.linspace(-1, 1, 51))
Z = f(X, Y, pts)

CS = plt.contour(X, Y, Z, 20)

tellme('Use mouse to select contour label locations, middle button to finish')
CL = plt.clabel(CS, manual=True)
```
