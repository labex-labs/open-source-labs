# Etiqueter les axes

Nous allons étiqueter manuellement les axes à l'aide de la fonction `text3d`. Cette fonction prend la position du texte, le texte à afficher, l'axe à considérer comme la troisième dimension et d'autres paramètres.

```python
def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    """
    Trace la chaîne *s* sur les axes *ax*, avec la position *xyz*, la taille *size*
    et l'angle de rotation *angle*. *zdir* indique l'axe qui doit être considéré
    comme la troisième dimension. *usetex* est un booléen indiquant si la chaîne
    doit être passée à travers un sous-processus LaTeX ou non. Tous les autres
    arguments clés sont transmis à `.transform_path`.

    Note: zdir affecte l'interprétation de xyz.
    """
    x, y, z = xyz
    if zdir == "y":
        xy1, z1 = (x, z), y
    elif zdir == "x":
        xy1, z1 = (y, z), x
    else:
        xy1, z1 = (x, y), z

    text_path = TextPath((0, 0), s, size=size, usetex=usetex)
    trans = Affine2D().rotate(angle).translate(xy1[0], xy1[1])

    p1 = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p1)
    art3d.pathpatch_2d_to_3d(p1, z=z1, zdir=zdir)


text3d(ax, (4, -2, 0), "X-axis", zdir="z", size=.5, usetex=False,
       ec="none", fc="k")
text3d(ax, (12, 4, 0), "Y-axis", zdir="z", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
text3d(ax, (12, 10, 4), "Z-axis", zdir="y", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
```
