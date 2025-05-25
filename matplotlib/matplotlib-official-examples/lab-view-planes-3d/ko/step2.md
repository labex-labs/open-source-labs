# 축 주석 함수 정의

각 기본 3D 뷰 평면에 해당 각도를 레이블링하기 위해 나중에 사용할 `annotate_axes` 함수를 정의합니다.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
