# 플롯에 컬러바 추가

이제 Matplotlib 의 `make_axes_locatable` 함수를 사용하여 각 서브플롯에 컬러바 (colorbar) 를 추가합니다. 이 함수는 기존 axes 를 가져와 새로운 `AxesDivider`에 추가하고 `AxesDivider`를 반환합니다. `AxesDivider`의 `append_axes` 메서드를 사용하여 원래 axes 의 지정된 측면 ("top", "right", "bottom", 또는 "left") 에 새로운 axes 를 생성할 수 있습니다.

```python
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
cb1 = fig.colorbar(im1, cax=cax1)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("top", size="7%", pad="2%")
cb2 = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cax2.xaxis.set_ticks_position("top")
```
