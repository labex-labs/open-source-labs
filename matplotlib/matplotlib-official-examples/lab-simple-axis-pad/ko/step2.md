# 축 설정 함수 정의

다음으로, 플롯의 극좌표 투영을 설정하는 `setup_axes()` 함수를 정의합니다. 이 함수는 `GridHelperCurveLinear`를 사용하여 직사각형 상자에 극좌표 투영을 생성합니다. 또한 플롯의 범위를 설정하고 `ax1` 객체를 반환합니다.

```python
def setup_axes(fig, rect):
    # Define the PolarAxes transform and the extreme finder
    tr = Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20, lon_cycle=360, lat_cycle=None, lon_minmax=None, lat_minmax=(0, np.inf))

    # Define the grid locators and formatters
    grid_locator1 = angle_helper.LocatorDMS(12)
    grid_locator2 = grid_finder.MaxNLocator(5)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Define the GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(tr, extreme_finder=extreme_finder, grid_locator1=grid_locator1, grid_locator2=grid_locator2, tick_formatter1=tick_formatter1)

    # Create the axis object and set its limits
    ax1 = fig.add_subplot(rect, axes_class=axisartist.Axes, grid_helper=grid_helper)
    ax1.axis[:].set_visible(False)
    ax1.set_aspect(1.)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    return ax1
```
