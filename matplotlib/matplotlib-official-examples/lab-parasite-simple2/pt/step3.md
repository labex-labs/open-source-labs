# Criar o Gráfico

Agora criaremos o gráfico usando as funções `HostAxes` e `twin()` do módulo `parasite_axes`. `HostAxes` é usado para criar o gráfico principal, e `twin()` é usado para criar o eixo y secundário.

```python
fig = plt.figure()

# Criar objeto HostAxes
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# Criar eixo y secundário com coordenadas transformadas
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# Plotar os dados
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# Definir os rótulos dos eixos
ax_kms.axis["bottom"].set_label("Velocidade linear a 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Movimento Próprio [$''$/yr]")

# Ocultar os rótulos dos ticks no eixo y secundário
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# Definir os limites do gráfico
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
