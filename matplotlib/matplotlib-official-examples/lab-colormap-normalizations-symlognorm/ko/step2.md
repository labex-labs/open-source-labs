# 합성 데이터 생성

이 단계에서는 음수 1 개와 양수 1 개, 총 두 개의 험프 (hump) 로 구성된 합성 데이터 세트를 생성합니다. 양수 험프는 음수 험프보다 8 배 더 큰 진폭을 갖습니다. 그런 다음 `SymLogNorm`을 적용하여 데이터를 시각화합니다.

```python
def rbf(x, y):
    return 1.0 / (1 + 5 * ((x ** 2) + (y ** 2)))

N = 200
gain = 8
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = rbf(X + 0.5, Y + 0.5)
Z2 = rbf(X - 0.5, Y - 0.5)
Z = gain * Z1 - Z2

shadeopts = {'cmap': 'PRGn', 'shading': 'gouraud'}
colormap = 'PRGn'
lnrwidth = 0.5
```
