# 사용자 정의 컬러맵 생성

Matplotlib 는 또한 사용자 정의 컬러맵을 생성하는 기능을 제공합니다. 이는 내장 컬러맵이 데이터의 원하는 표현을 제공하지 않을 때 유용할 수 있습니다.

```python
import matplotlib.colors as mcolors

# 색상 목록과 해당 값을 정의합니다.
colors = [(0, 'red'), (0.5, 'green'), (1, 'blue')]

# 색상 목록에서 LinearSegmentedColormap 객체를 생성합니다.
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
