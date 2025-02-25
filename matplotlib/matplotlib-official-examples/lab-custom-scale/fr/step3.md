# Implémentez la classe MercatorLatitudeTransform

Dans la classe `MercatorLatitudeScale`, nous allons définir la classe `MercatorLatitudeTransform` qui transformera réellement les données. Cette classe héritera de `mtransforms.Transform`.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # Il existe deux membres de valeur qui doivent être définis.
        # ``input_dims`` et ``output_dims`` spécifient le nombre de dimensions
        # d'entrée et de dimensions de sortie de la transformation.
        # Ces informations sont utilisées par le cadre de transformation pour
        # effectuer certaines vérifications d'erreur et empêcher les
        # transformations incompatibles d'être connectées ensemble. Lors de
        # la définition de transformations pour une échelle, qui sont, par
        # définition, séparables et n'ont qu'une seule dimension, ces
        # membres devraient toujours être définis sur 1.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            Cette transformation prend un tableau numpy et renvoie une copie transformée.
            Étant donné que la plage de l'échelle Mercator est limitée par le
            seuil spécifié par l'utilisateur, le tableau d'entrée doit être masqué
            pour ne contenir que des valeurs valides. Matplotlib gérera les tableaux
            masqués et supprimera les données en dehors de la plage du tracé.
            Cependant, le tableau renvoyé *doit* avoir la même forme que le
            tableau d'entrée, car ces valeurs doivent rester synchronisées avec
            les valeurs dans l'autre dimension.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Redéfinissez cette méthode pour que Matplotlib sache comment obtenir
            la transformation inverse de cette transformation.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
