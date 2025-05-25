# 축 외부 레이블 지정

축 외부에 레이블을 지정하되 서로 정렬되도록 하는 것이 더 나을 수 있습니다. 이 경우 약간 다른 변환 (transform) 을 사용합니다.

```python
for label, ax in axs.items():
    # label physical distance to the left and up:
    trans = mtransforms.ScaledTranslation(-20/72, 7/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', va='bottom', fontfamily='serif')
```
