# 플롯 생성

이제 parasite_axes 모듈의 HostAxes 및 twin() 함수를 사용하여 플롯을 생성합니다. HostAxes 는 메인 플롯을 생성하는 데 사용되며, twin() 은 보조 y 축을 생성하는 데 사용됩니다.

```python
fig = plt.figure()

# HostAxes 객체 생성
ax_kms = fig.add_subplot(axes_class=HostAxes, aspect=1)

# 변환된 좌표를 사용하여 보조 y 축 생성
aux_trans = mtransforms.Affine2D().scale(pm_to_kms, 1.)
ax_pm = ax_kms.twin(aux_trans)

# 데이터 플롯
for n, ds, dse, w, we in obs:
    time = ((2007 + (10. + 4/30.)/12) - 1988.5)
    v = ds / time * pm_to_kms
    ve = dse / time * pm_to_kms
    ax_kms.errorbar([v], [w], xerr=[ve], yerr=[we], color="k")

# 축 레이블 설정
ax_kms.axis["bottom"].set_label("Linear velocity at 2.3 kpc [km/s]")
ax_kms.axis["left"].set_label("FWHM [km/s]")
ax_pm.axis["top"].set_label(r"Proper Motion [$''$/yr]")

# 보조 y 축의 눈금 레이블 숨기기
ax_pm.axis["right"].major_ticklabels.set_visible(False)

# 플롯 제한 설정
ax_kms.set_xlim(950, 3700)
ax_kms.set_ylim(950, 3100)
```
