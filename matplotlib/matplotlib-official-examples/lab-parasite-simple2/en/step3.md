# Create the Plot

We will now create the plot using the HostAxes and twin() functions from the parasite_axes module. HostAxes is used to create the main plot, and twin() is used to create the secondary y-axis.

```python
fig = plt.figure()

# Create HostAxes object
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Create secondary y-axis with transformed coordinates
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Plot the data
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Set the axis labels
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# Hide the tick labels on the secondary y-axis
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Set the plot limits
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
