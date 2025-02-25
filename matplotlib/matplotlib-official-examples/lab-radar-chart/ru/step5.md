# Определить методы `set_varlabels`, `_gen_axes_patch` и `_gen_axes_spines`

Внутри класса `RadarAxes` мы также определим методы `set_varlabels`, `_gen_axes_patch` и `_gen_axes_spines`. Эти методы будут настраивать метки переменных, генерировать участок осей и генерировать шипы осей соответственно.

```python
class RadarAxes(PolarAxes):
    # код для класса RadarAxes будет здесь

    def set_varlabels(self, labels):
        self.set_thetagrids(np.degrees(theta), labels)

    def _gen_axes_patch(self):
        if frame == 'circle':
            return Circle((0.5, 0.5), 0.5)
        elif frame == 'polygon':
            return RegularPolygon((0.5, 0.5), num_vars,
                                  radius=.5, edgecolor="k")
        else:
            raise ValueError("Unknown value for 'frame': %s" % frame)

    def _gen_axes_spines(self):
        if frame == 'circle':
            return super()._gen_axes_spines()
        elif frame == 'polygon':
            spine = Spine(axes=self,
                          spine_type='circle',
                          path=Path.unit_regular_polygon(num_vars))
            spine.set_transform(Affine2D().scale(.5).translate(.5,.5)
                                + self.transAxes)
            return {'polar': spine}
        else:
            raise ValueError("Unknown value for 'frame': %s" % frame)
```
