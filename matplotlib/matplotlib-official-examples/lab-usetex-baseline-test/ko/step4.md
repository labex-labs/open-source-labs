# 플롯에 테스트 문자열 추가

각 서브플롯에 서로 다른 스타일과 위치를 가진 네 개의 테스트 문자열을 추가합니다. `text()` 메서드를 사용하여 서브플롯에 텍스트를 추가합니다.

```python
test_strings = ["lg", r"$\frac{1}{2}\pi$", r"$p^{3^A}$", r"$p_{3_2}$"]
for ax, usetex in zip(axs, [False, True]):
    ax.axvline(0, color="r")
    for i, s in enumerate(test_strings):
        ax.axhline(i, color="r")
        ax.text(0., 3 - i, s,
                usetex=usetex,
                verticalalignment="baseline",
                size=50,
                bbox=dict(pad=0, ec="k", fc="none"))
```
