# Definieren der Klasse `AngleAnnotation`

```python
class AngleAnnotation(Arc):
    """
    Zeichnet einen Bogen zwischen zwei Vektoren, der im Anzeigeraum kreisförmig erscheint.
    """
    def __init__(self, xy, p1, p2, size=75, unit="points", ax=None,
                 text="", textposition="inside", text_kw=None, **kwargs):
        """
        Parameter
        ----------
        xy, p1, p2 : tuple oder Array von zwei Fließkommazahlen
            Mittelpunktsposition und zwei Punkte. Der Winkelbezeichner wird zwischen
            den zwei Vektoren gezeichnet, die jeweils *p1* und *p2* mit *xy* verbinden.
            Die Einheiten sind Datenkoordinaten.

        size : float
            Durchmesser des Winkelbezeichners in der von *unit* angegebenen Einheit.

        unit : str
            Einer der folgenden Zeichenketten, um die Einheit von *size* anzugeben:

            * "pixels": Pixel
            * "points": Punkte, verwenden Sie Punkte anstelle von Pixeln, um keine
              Abhängigkeit von der DPI zu haben
            * "axes width", "axes height": relative Einheiten der Achsenbreite, -höhe
            * "axes min", "axes max": Minimum oder Maximum der relativen Achsen
              Breite, Höhe

        ax : `matplotlib.axes.Axes`
            Die Achse, der der Winkelbezeichner hinzugefügt werden soll.

        text : str
            Der Text, um den Winkel zu markieren.

        textposition : {"inside", "outside", "edge"}
            Ob der Text innerhalb oder außerhalb des Bogens angezeigt werden soll. "edge" kann für benutzerdefinierte Positionen verwendet werden, die am Rand des Bogens befestigt sind.

        text_kw : dict
            Dictionary von Argumenten, die an die Annotation übergeben werden.

        **kwargs
            Weitere Parameter werden an `matplotlib.patches.Arc` übergeben. Verwenden Sie dies, um Farbe, Linienbreite usw. des Bogens anzugeben.

        """
        self.ax = ax or plt.gca()
        self._xydata = xy  # in Datenkoordinaten
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
        faktor = 1.
        if self.unit == "points":
            faktor = self.ax.figure.dpi / 72.
        elif self.unit[:4] == "axes":
            b = TransformedBbox(Bbox.unit(), self.ax.transAxes)
            dic = {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            faktor = dic[self.unit[5:]]
        return self.size * faktor

    def set_size(self, size):
        self.size = size

    def get_center_in_pixels(self):
        """gibt den Mittelpunkt in Pixeln zurück"""
        return self.ax.transData.transform(self._xydata)

    def set_center(self, xy):
        """setzt den Mittelpunkt in Datenkoordinaten"""
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

    # Überschreiben Sie die Attribute der Arc, um immer Werte im Pixelraum zu liefern
    _center = property(get_center_in_pixels, set_center)
    theta1 = property(get_theta1, set_theta)
    theta2 = property(get_theta2, set_theta)
    width = property(get_size, set_size)
    height = property(get_size, set_size)

    # Die folgenden beiden Methoden sind erforderlich, um die Textposition zu aktualisieren.
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
