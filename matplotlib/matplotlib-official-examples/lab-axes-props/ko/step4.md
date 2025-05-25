# 축 눈금 및 그리드 속성 사용자 정의

`grid()` 및 `tick_params()` 함수를 사용하여 축 눈금 및 그리드 속성을 사용자 정의할 수 있습니다. 이 예제에서는 눈금 레이블의 색상과 크기, 그리드 선의 너비와 스타일을 변경합니다.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
