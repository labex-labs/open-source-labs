# 그리드 헬퍼 정의

이 단계에서는 극좌표 곡선을 생성하는 데 사용될 그리드 헬퍼를 정의합니다. `GridHelperCurveLinear`를 사용하여 그리드 헬퍼를 정의합니다.

```python
from mpl_toolkits.axisartist import GridHelperCurveLinear, HostAxes
import mpl_toolkits.axisartist.angle_helper as angle_helper

# Define the grid helper
extreme_finder = angle_helper.ExtremeFinderCycle(20,
                                                 20,
                                                 lon_cycle=360,
                                                 lat_cycle=None,
                                                 lon_minmax=None,
                                                 lat_minmax=(0, np.inf),
                                                 )
grid_locator1 = angle_helper.LocatorDMS(12)
tick_formatter1 = angle_helper.FormatterDMS()

grid_helper = GridHelperCurveLinear(tr,
                                    extreme_finder=extreme_finder,
                                    grid_locator1=grid_locator1,
                                    tick_formatter1=tick_formatter1
                                    )
```
