# 축 내부 레이블 지정

서브플롯에 레이블을 지정하는 가장 간단한 방법은 축 내부에 레이블을 넣는 것입니다. `ax.text` 메서드를 사용하여 이를 수행할 수 있습니다. 각 서브플롯을 반복하고 `ax.transAxes`를 사용하여 축 내부에 레이블을 추가합니다.

```python
for label, ax in axs.items():
    # label physical distance in and down:
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif',
            bbox=dict(facecolor='0.7', edgecolor='none', pad=3.0))
```
