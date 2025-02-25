# Projection polaire dans un cadre rectangulaire

Ensuite, nous allons créer une projection polaire dans un cadre rectangulaire en utilisant `GridHelperCurveLinear`. Nous utiliserons une transformation `Affine2D` pour convertir les coordonnées en degrés en radians, et `PolarAxes.PolarTransform` pour créer la projection polaire. Nous utiliserons également `angle_helper.ExtremeFinderCycle` pour trouver les extrêmes de la projection polaire, et `angle_helper.LocatorDMS` et `angle_helper.FormatterDMS` pour formater les étiquettes d'échelle. Le code suivant illustre ce processus :

```python
def curvelinear_test2(fig):
    # Définir la transformation personnalisée
    tr = Affine2D().scale(np.pi/180, 1) + PolarAxes.PolarTransform()

    # Définir le chercheur d'extrêmes, le localisateur de grille et le formateur d'étiquettes d'échelle
    extreme_finder = angle_helper.ExtremeFinderCycle(
        nx=20, ny=20,
        lon_cycle=360, lat_cycle=None,
        lon_minmax=None, lat_minmax=(0, np.inf),
    )
    grid_locator1 = angle_helper.LocatorDMS(12)
    tick_formatter1 = angle_helper.FormatterDMS()

    # Créer un objet GridHelperCurveLinear
    grid_helper = GridHelperCurveLinear(
        tr, extreme_finder=extreme_finder,
        grid_locator1=grid_locator1, tick_formatter1=tick_formatter1)
    ax1 = fig.add_subplot(
        1, 2, 2, axes_class=HostAxes, grid_helper=grid_helper)

    # Rendre les étiquettes d'échelle de l'axe droit et supérieur visibles
    ax1.axis["right"].major_ticklabels.set_visible(True)
    ax1.axis["top"].major_ticklabels.set_visible(True)

    # Faire en sorte que l'axe droit affiche les étiquettes d'échelle pour la première coordonnée (angle)
    ax1.axis["right"].get_helper().nth_coord_ticks = 0

    # Faire en sorte que l'axe inférieur affiche les étiquettes d'échelle pour la deuxième coordonnée (rayon)
    ax1.axis["bottom"].get_helper().nth_coord_ticks = 1

    # Définir le rapport d'aspect et les limites du sous-graphique
    ax1.set_aspect(1)
    ax1.set_xlim(-5, 12)
    ax1.set_ylim(-5, 10)

    # Ajouter des lignes de grille au sous-graphique
    ax1.grid(True, zorder=0)

    # Créer un axe parasite avec la transformation donnée
    ax2 = ax1.get_aux_axes(tr)

    # Tout ce que vous tracez dans ax2 correspondra aux échelles et aux grilles d'ax1.
    ax2.plot(np.linspace(0, 30, 51), np.linspace(10, 10, 51), linewidth=2)

    ax2.pcolor(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
               np.arange(9).reshape((3, 3)))
    ax2.contour(np.linspace(0, 90, 4), np.linspace(0, 10, 4),
                np.arange(16).reshape((4, 4)), colors="k")

fig = plt.figure(figsize=(7, 4))
curvelinear_test2(fig)
plt.show()
```
