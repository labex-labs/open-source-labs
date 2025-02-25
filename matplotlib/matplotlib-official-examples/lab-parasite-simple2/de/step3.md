# Den Graphen erstellen

Wir werden nun den Graphen mit den Funktionen HostAxes und twin() aus dem parasite_axes-Modul erstellen. HostAxes wird verwendet, um den Hauptgraphen zu erstellen, und twin() wird verwendet, um die sekundäre y-Achse zu erstellen.

```python
fig = plt.figure()

# Erstellen eines HostAxes-Objekts
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Erstellen der sekundären y-Achse mit transformierten Koordinaten
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Plotten der Daten
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Festlegen der Achsenbeschriftungen
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# Ausblenden der Strichmarkenbeschriftungen auf der sekundären y-Achse
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Festlegen der Graphengrenzen
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
