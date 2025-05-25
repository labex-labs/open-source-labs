# 확대된 플롯 생성

이번에는 `markevery`가 확대된 플롯에서 어떻게 동작하는지 보여주기 위해 또 다른 일련의 서브플롯을 생성합니다. 정수 기반의 서브샘플링은 기본 데이터에서 포인트를 선택하며 뷰 (view) 와 독립적인 반면, 부동 소수점 기반의 서브샘플링은 Axes 대각선과 관련이 있으며 표시된 데이터 범위를 변경합니다.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
