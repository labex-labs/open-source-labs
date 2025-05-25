# 플롯 생성

이제 `PathPatch` 객체를 축 (axes) 에 추가하고 곡선 위에 있어야 하는 빨간색 점을 플로팅하여 플롯을 생성할 수 있습니다. 또한 플롯의 제목을 `'Bezier Curve'`로 설정합니다.

```python
fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```

최종 코드는 다음과 같습니다.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath

Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])

bezier_patch = mpatches.PathPatch(bezier_path, fc="none")

fig, ax = plt.subplots()

ax.add_patch(bezier_patch)
ax.plot([0.75], [0.25], "ro")
ax.set_title('Bezier Curve')

plt.show()
```
