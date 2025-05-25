# 나선형 생성

```python
nverts = 50
npts = 100

# Make some spirals
r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])
```

다음 단계는 Numpy 를 사용하여 나선형을 생성하는 것입니다. sin 및 cos 함수를 사용하여 나선형을 생성합니다.
