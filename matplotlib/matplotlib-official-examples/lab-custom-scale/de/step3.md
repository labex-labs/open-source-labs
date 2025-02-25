# Implementieren der MercatorLatitudeTransform-Klasse

Innerhalb der `MercatorLatitudeScale`-Klasse definieren wir die `MercatorLatitudeTransform`-Klasse, die die Daten tatsächlich transformieren wird. Diese Klasse erbt von `mtransforms.Transform`.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # Es gibt zwei Wertmitglieder, die definiert werden müssen.
        # ``input_dims`` und ``output_dims`` geben die Anzahl der Eingangs-
        # und Ausgangsdimensionen der Transformation an.
        # Diese werden vom Transformationsframework verwendet, um einige
        # Fehlerprüfungen durchzuführen und zu verhindern, dass inkonsistente
        # Transformationen miteinander verbunden werden. Wenn Transformations-
        # funktionen für eine Skala definiert werden, die, per Definition,
        # separierbar und nur eine Dimension haben, sollten diese Mitglieder
        # immer auf 1 gesetzt werden.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            Diese Transformation nimmt ein Numpy-Array und gibt eine transformierte
            Kopie zurück. Da der Bereich der Mercator-Skala durch den
            benutzerdefinierten Schwellenwert begrenzt ist, muss das Eingangs-
            array maskiert werden, um nur gültige Werte zu enthalten. Matplotlib
            wird maskierte Arrays verarbeiten und die außerhalb des Bereichs
            liegenden Daten aus dem Plot entfernen. Allerdings muss das
            zurückgegebene Array *genau* die gleiche Form wie das Eingangs-
            array haben, da diese Werte mit den Werten in der anderen Dimension
            synchron bleiben müssen.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Überschreiben Sie diese Methode, damit Matplotlib weiß, wie die
            inverse Transformation für diese Transformation berechnet wird.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
