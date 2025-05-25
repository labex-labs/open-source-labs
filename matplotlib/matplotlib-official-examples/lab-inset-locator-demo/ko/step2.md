# 삽입 축 (Inset Axes) 생성

다음으로, 각 서브플롯에 삽입 축을 생성합니다. `inset_axes()` 메서드를 사용하여 삽입 축을 생성합니다. 서로 다른 크기와 위치의 네 개의 삽입을 생성합니다.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# 기본 오른쪽 상단 위치에 너비 1.3 인치, 높이 0.9 인치의 삽입 생성
axins = inset_axes(ax, width=1.3, height=0.9)

# 부모 축의 경계 상자의 30% 너비와 40% 높이의 삽입을 왼쪽 하단 모서리 (loc=3) 에 생성
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# 두 번째 서브플롯에 혼합된 사양의 삽입 생성;
# 너비는 부모 축의 경계 상자의 30% 이고
# 높이는 왼쪽 상단 모서리 (loc=2) 에서 1 인치
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# 오른쪽 하단 모서리 (loc=4) 에 borderpad=1, 즉
# 부모 축에 10 포인트 패딩 (10pt 가 기본 글꼴 크기) 이 있는 삽입 생성
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
