# Etiquetar los ejes

Etiquetaremos manualmente los ejes utilizando la función `text3d`. La función toma la posición del texto, el texto a mostrar, el eje que se considerará como la tercera dimensión y otros parámetros.

```python
def text3d(ax, xyz, s, zdir="z", size=None, angle=0, usetex=False, **kwargs):
    """
    Dibuja la cadena *s* en los ejes *ax*, con posición *xyz*, tamaño *size*,
    y ángulo de rotación *angle*. *zdir* indica el eje que se considerará como
    la tercera dimensión. *usetex* es un booleano que indica si la cadena
    debe pasar por un subproceso de LaTeX o no. Cualquier otro argumento
    de palabras clave adicional se pasa a `.transform_path`.

    Nota: zdir afecta la interpretación de xyz.
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


text3d(ax, (4, -2, 0), "Eje X", zdir="z", size=.5, usetex=False,
       ec="none", fc="k")
text3d(ax, (12, 4, 0), "Eje Y", zdir="z", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
text3d(ax, (12, 10, 4), "Eje Z", zdir="y", size=.5, usetex=False,
       angle=np.pi / 2, ec="none", fc="k")
```
