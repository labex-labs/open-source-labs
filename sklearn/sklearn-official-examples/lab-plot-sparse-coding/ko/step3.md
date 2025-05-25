# 신호 생성

Matplotlib 을 사용하여 신호를 생성하고 시각화합니다.

```python
resolution = 1024
subsampling = 3  # 서브샘플링 계수
width = 100
n_components = resolution // subsampling

# 신호 생성
y = np.linspace(0, resolution - 1, resolution)
first_quarter = y < resolution / 4
y[first_quarter] = 3.0
y[np.logical_not(first_quarter)] = -1.0

# 신호 시각화
plt.figure()
plt.plot(y)
plt.title("원본 신호")
plt.show()
```
