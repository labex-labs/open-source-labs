# SkewXAxes 클래스 정의

SkewXAxes 클래스는 skew-xaxes 를 투영 (projection) 으로 등록하고 적절한 변환을 설정하는 것을 처리합니다. 필요에 따라 표준 스파인 (spines) 및 축 (axes) 인스턴스를 재정의합니다.

```python
class SkewXAxes(Axes):
    name = 'skewx'

    def _init_axis(self):
        super()._init_axis()
        self.xaxis = SkewXAxis(self)
        self.spines.top.register_axis(self.xaxis)
        self.spines.bottom.register_axis(self.xaxis)

    def _gen_axes_spines(self):
        spines = {'top': SkewSpine.linear_spine(self, 'top'),
                  'bottom': mspines.Spine.linear_spine(self, 'bottom'),
                  'left': mspines.Spine.linear_spine(self, 'left'),
                  'right': mspines.Spine.linear_spine(self, 'right')}
        return spines

    def _set_lim_and_transforms(self):
        super()._set_lim_and_transforms()
        rot = 30
        self.transDataToAxes = (self.transScale + self.transLimits + transforms.Affine2D().skew_deg(rot, 0))
        self.transData = self.transDataToAxes + self.transAxes
        self._xaxis_transform = (transforms.blended_transform_factory(
            self.transScale + self.transLimits, transforms.IdentityTransform()) + transforms.Affine2D().skew_deg(rot, 0) + self.transAxes)

    @property
    def lower_xlim(self):
        return self.axes.viewLim.intervalx

    @property
    def upper_xlim(self):
        pts = [[0., 1.], [1., 1.]]
        return self.transDataToAxes.inverted().transform(pts)[:, 0]
```
