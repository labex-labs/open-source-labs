# Definir la clase `AngleAnnotation`

```python
class AngleAnnotation(Arc):
    """
    Dibuja un arco entre dos vectores que parece circular en el espacio de visualización.
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parámetros
        ----------
        xy, p1, p2 : tupla o matriz de dos flotantes
            Posición del centro y dos puntos. La anotación de ángulo se dibuja entre
            los dos vectores que conectan *p1* y *p2* con *xy*, respectivamente.
            Las unidades son coordenadas de datos.

        size : float
            Diámetro de la anotación de ángulo en las unidades especificadas por *unit*.

        unit : str
            Una de las siguientes cadenas para especificar la unidad de *size*:

            * "pixels": píxeles
            * "points": puntos, use puntos en lugar de píxeles para no depender del DPI
            * "axes width", "axes height": unidades relativas del ancho, alto de los Ejes
            * "axes min", "axes max": mínimo o máximo de la anchura, altura relativa de los Ejes

        ax : `matplotlib.axes.Axes`
            Los Ejes donde se agregará la anotación de ángulo.

        text : str
            El texto para marcar el ángulo.

        textposition : {"inside", "outside", "edge"}
            Si se muestra el texto dentro o fuera del arco. "edge" se puede usar
            para posiciones personalizadas ancladas en el borde del arco.

        text_kw : dict
            Diccionario de argumentos pasados a la Anotación.

        **kwargs
            Otros parámetros se pasan a `matplotlib.patches.Arc`. Use esto
            para especificar el color, el ancho de línea, etc. del arco.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # en coordenadas de datos
        self.vec1 = p1
        self.vec2 = p2
        self.size = size
        self.unit = unit
        self.textposition = textposition

        super().__init__(self._xydata, size, size, angle=0.0,
                         theta1=self.theta1, theta2=self.theta2, **kwargs)

        self.set_transform(IdentityTransform())
        self.ax.add_patch(self)

        self.kw = dict(ha="center", va="center",
                       xycoords=IdentityTransform(),
                       xytext=(0, 0), textcoords="offset points",
                       annotation_clip=True)
        self.kw.update(text_kw or {})
        self.text = ax.annotate(text, xy=self._center, **self.kw)

    def get_size(self):
        factor = 1.
        if self.unit == "points":
            factor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.unit(), self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor = dic[self.unit[5:]]
        return self.size * factor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """devuelve el centro en píxeles"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """establece el centro en coordenadas de datos"""
        self._xydata = xy

    def get_theta(self, vec):
        vec_in_pixels = self.ax.transData.transform(vec) - self._center
        return np.rad2deg(np.arctan2(vec_in_pixels[1], vec_in_pixels[0]))

    def get_theta1(self):
        return self.get_theta(self.vec1)

    def get_theta2(self):
        return self.get_theta(self.vec2)

    def set_theta(self, angle):
        pass

    # Redefine los atributos de Arc para siempre dar valores en el espacio de píxeles
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # Los siguientes dos métodos son necesarios para actualizar la posición del texto.
    def draw(self, renderer):
        self.update_text()
        super().draw(renderer)

    def update_text(self):
        c = self._center
        s = self.get_size()
        angle_span = (self.theta2 - self.theta1) % 360
        angle = np.deg2rad(self.theta1 + angle_span / 2)
        r = s / 2
        if self.textposition == "inside":
            r = s / np.interp(angle_span, [60, 90, 135, 180],
                                          [3.3, 3.5, 3.8, 4])
        self.text.xy = c + r * np.array([np.cos(angle), np.sin(angle)])
        if self.textposition == "outside":
            def R90(a, r, w, h):
                if a < np.arctan(h/2/(r+w/2)):
                    return np.sqrt((r+w/2)**2 + (np.tan(a)*(r+w/2))**2)
                else:
                    c = np.sqrt((w/2)**2+(h/2)**2)
                    T = np.arcsin(c * np.cos(np.pi/2 - a + np.arcsin(h/2/c))/r)
                    xy = r * np.array([np.cos(a + T), np.sin(a + T)])
                    xy += np.array([w/2, h/2])
                    return np.sqrt(np.sum(xy**2))

            def R(a, r, w, h):
                aa = (a % (np.pi/4))*((a % (np.pi/2)) <= np.pi/4) + \
                     (np.pi/4 - (a % (np.pi/4)))*((a % (np.pi/2)) >= np.pi/4)
                return R90(aa, r, *[w, h][::int(np.sign(np.cos(2*a)))])

            bbox = self.text.get_window_extent()
            X = R(angle, r, bbox.width, bbox.height)
            trans = self.ax.figure.dpi_scale_trans.inverted()
            offs = trans.transform(((X-s/2), 0))[0] * 72
            self.text.set_position([offs*np.cos(angle), offs*np.sin(angle)])
```
