# 플롯 생성

`subplots` 함수를 사용하여 2x2 그리드의 서브플롯 (subplot) 을 생성합니다. 그런 다음, `plot` 함수를 사용하여 각 서브플롯에 데이터를 플롯합니다.

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # scalars are interpreted in current units

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # cm are converted to inches
```
