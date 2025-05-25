# GeoAxes 클래스 생성

`GeoAxes`라는 지리 투영법 (geographic projections) 을 위한 추상 기본 클래스를 생성합니다.

```python
class GeoAxes(Axes):
    """
    지리 투영법을 위한 추상 기본 클래스
    """

    class ThetaFormatter(Formatter):
        """
        세타 눈금 레이블의 형식을 지정하는 데 사용됩니다. 네이티브
        단위인 라디안을 도 (degree) 로 변환하고 도 기호를 추가합니다.
        """
        def __init__(self, round_to=1.0):
            self._round_to = round_to

        def __call__(self, x, pos=None):
            degrees = round(np.rad2deg(x) / self._round_to) * self._round_to
            return f"{degrees:0.0f}\N{DEGREE SIGN}"

    RESOLUTION = 75

    def _init_axis(self):
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        # GeoAxes.xaxis.clear() 가 작동할 때까지,
        # Axes._init_axis() 에서 수행되는 것처럼, xaxis 또는 yaxis 를 스파인 (spines) 에 등록하지 마십시오.
        # self.spines['geo'].register_axis(self.yaxis)

    def clear(self):
        # docstring 상속
        super().clear()

        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        # 왜 y 축 눈금 레이블을 켜야 하지만,
        # x 축 눈금 레이블은 이미 켜져 있습니까?

        self.grid(rcParams['axes.grid'])

        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
```
