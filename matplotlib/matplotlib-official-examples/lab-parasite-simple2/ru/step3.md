# Создание графика

Теперь мы создадим график с использованием функций HostAxes и twin() из модуля parasite_axes. HostAxes используется для создания основного графика, а twin() - для создания вторичной оси y.

```python
fig = plt.figure()

# Создаем объект HostAxes
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Создаем вторичную ось y с преобразованными координатами
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Строим данные
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Задаем метки осей
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# Скрываем метки делений на вторичной оси y
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Задаем пределы графика
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
