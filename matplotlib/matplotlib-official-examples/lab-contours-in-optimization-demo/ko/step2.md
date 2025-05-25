# 조사 벡터 및 행렬 설정

다음으로, 조사 벡터와 행렬을 설정합니다. 디스크 로딩과 기어비를 설계합니다.

```python
nx = 101
ny = 105

# Set up survey vectors
xvec = np.linspace(0.001, 4.0, nx)
yvec = np.linspace(0.001, 4.0, ny)

# Set up survey matrices.  Design disk loading and gear ratio.
x1, x2 = np.meshgrid(xvec, yvec)
```
