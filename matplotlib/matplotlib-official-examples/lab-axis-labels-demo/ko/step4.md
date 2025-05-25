# 컬러바 레이블 위치 설정

`colorbar` 메서드와 `set_label` 메서드를 사용하여 컬러바 레이블의 위치를 설정할 수 있습니다. 위치는 `'top'`, `'bottom'`, `'left'`, 또는 `'right'`로 설정할 수 있습니다. 이 예제에서는 위치를 `'top'`으로 설정합니다.

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
