# プロットの作成

ここでは、parasite_axes モジュールの HostAxes と twin() 関数を使ってプロットを作成します。HostAxes はメインプロットを作成するために使用し、twin() は 2 次 y 軸を作成するために使用します。

```python
fig = plt.figure()

# HostAxes オブジェクトを作成
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# 変換された座標で 2 次 y 軸を作成
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# データをプロット
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# 軸のラベルを設定
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# 2 次 y 軸の目盛りラベルを非表示にする
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# プロットの範囲を設定
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
