# Definir los métodos `set_varlabels`, `_gen_axes_patch` y `_gen_axes_spines`

Dentro de la clase `RadarAxes`, también definiremos los métodos `set_varlabels`, `_gen_axes_patch` y `_gen_axes_spines`. Estos métodos establecerán las etiquetas de las variables, generarán el recuadro de los ejes y generarán las espinas de los ejes, respectivamente.

```python
class RadarAxes(PolarAxes):
    # código de la clase RadarAxes va aquí

    def set_varlabels(self, labels):
        self.set_thetagrids(np.degrees(theta), labels)

    def _gen_axes_patch(self):
        if frame == 'circle':
            return Circle((0.5, 0.5), 0.5)
        elif frame == 'polygon':
            return RegularPolygon((0.5, 0.5), num_vars,
                                  radius=.5, edgecolor="k")
        else:
            raise ValueError("Valor desconocido para 'frame': %s" % frame)

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
            raise ValueError("Valor desconocido para 'frame': %s" % frame)
```
