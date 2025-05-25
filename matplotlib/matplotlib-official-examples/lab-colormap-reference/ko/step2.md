# 간단한 컬러맵 생성

간단한 컬러맵을 생성하기 위해 `matplotlib.colors` 모듈에서 `ListedColormap` 클래스를 사용할 수 있습니다. 이 클래스는 색상 목록을 받아 해당 색상으로 컬러맵을 생성합니다.

```python
import matplotlib.colors as mcolors

# 색상 목록 정의
colors = ['red', 'green', 'blue']

# 색상 목록에서 ListedColormap 객체 생성
cmap = mcolors.ListedColormap(colors)
```
