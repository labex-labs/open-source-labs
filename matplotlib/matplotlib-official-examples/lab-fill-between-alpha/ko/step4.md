# `axhspan` 및 `axvspan`을 사용하여 축 범위 강조 표시하기

채워진 영역의 또 다른 유용한 사용법은 축 (Axes) 의 수평 또는 수직 범위를 강조 표시하는 것입니다. 이를 위해 Matplotlib 에는 헬퍼 함수 `axhspan`과 `axvspan`이 있습니다. 자세한 내용은 `axhspan_demo` 갤러리를 참조하십시오.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
ax.axvspan(6, 7, facecolor='r', alpha=0.5)

plt.show()
```
