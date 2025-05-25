# 중심 좌표 (Centered coordinates)

사용자는 종종 `.axes.Axes.pcolormesh`에 *Z*와 동일한 크기의 *X*와 *Y*를 전달하려는 경우가 있습니다. 이는 `shading='auto'`가 전달된 경우에도 허용됩니다 (기본값은 :rc:`pcolor.shading`에 의해 설정됨). Matplotlib 3.3 이전에는 `shading='flat'`이 *Z*의 마지막 열과 행을 삭제했지만, 이제는 오류를 발생시킵니다. 이것이 정말로 원하는 것이라면, *Z*의 마지막 행과 열을 수동으로 삭제하십시오.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # len = 10
y = np.arange(6)  # len = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
