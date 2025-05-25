# Y-Label 을 위한 공간 확보 및 축 조정

이 단계에서는 `make_axes_area_auto_adjustable` 메서드를 사용하여 두 축 모두에서 y-label 을 위한 공간을 확보합니다. 또한 `use_axes` 매개변수를 사용하여 조정할 축을 지정하고, `pad` 매개변수를 사용하여 축 사이의 간격을 조정합니다.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
