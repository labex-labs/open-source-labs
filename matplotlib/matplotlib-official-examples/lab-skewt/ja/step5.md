# SkewXAxes クラスを定義する

SkewXAxes クラスは、スキューX 軸を射影として登録することと、適切な変換を設定することを担当します。必要に応じて、標準のスパインと軸のインスタンスを上書きします。

```python
class SkewXAxes(Axes):
    name ='skewx'

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
