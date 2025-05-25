# 수직 컬러바의 눈금 레이블 사용자 정의

다음으로, 수직 컬러바의 눈금 레이블을 사용자 정의합니다. `colorbar`를 사용하여 컬러바를 생성하고 `ticks` 매개변수를 사용하여 눈금 위치를 지정합니다. 그런 다음 컬러바 객체의 `ax` 속성에서 `set_yticklabels`을 사용하여 눈금 레이블을 설정합니다.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
