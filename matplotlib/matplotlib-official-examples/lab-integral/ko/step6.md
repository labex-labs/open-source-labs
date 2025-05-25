# 적분 레이블 추가

`text`를 사용하여 플롯에 적분 레이블을 추가합니다. 레이블은 a 와 b 사이의 중간점에 맞춰져야 하며 mathtext 를 사용하여 서식을 지정해야 합니다.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
