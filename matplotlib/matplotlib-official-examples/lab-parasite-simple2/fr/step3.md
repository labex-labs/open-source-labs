# Créer le graphique

Nous allons maintenant créer le graphique en utilisant les fonctions HostAxes et twin() du module parasite_axes. HostAxes est utilisé pour créer le graphique principal, et twin() est utilisé pour créer le deuxième axe y.

```python
fig = plt.figure()

# Créer un objet HostAxes
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Créer le deuxième axe y avec des coordonnées transformées
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Tracer les données
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Définir les étiquettes des axes
ax_kms.axis["bottom"].set_label("Vitesse linéaire à 2,3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Mouvement propre [$''$/an]")

# Cacher les étiquettes d'échelle du deuxième axe y
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Définir les limites du graphique
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
