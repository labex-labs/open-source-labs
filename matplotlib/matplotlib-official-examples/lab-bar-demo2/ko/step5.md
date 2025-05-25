# 스칼라 또는 단위를 사용하여 x-limit 설정

이 단계에서는 스칼라 또는 단위를 사용하여 x-limit 을 설정합니다. `set_xlim` 메서드를 사용하여 x-limit 을 설정합니다. 두 번째 행과 첫 번째 열의 막대 그래프에 대해 현재 단위의 스칼라를 사용하여 x-limit 을 2 와 6 으로 설정합니다. 두 번째 행과 두 번째 열의 막대 그래프에 대해 단위를 사용하여 x-limit 을 2 cm 와 6 cm 로 설정합니다.

```python
axs[1, 0].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(2, 6)

axs[1, 1].bar(cms, cms, bottom=bottom, width=width, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(2 * cm, 6 * cm)
```
