# 서로 다른 스케일 파라미터 "linear_width"를 가진 "asinh" 그래프 비교

이제 서로 다른 스케일 파라미터 "linear_width"를 가진 "asinh" 그래프를 비교해 보겠습니다. 서로 다른 "linear_width" 값을 가진 세 개의 그래프를 플롯할 것입니다.

```python
fig2 = plt.figure(layout='constrained')
axs = fig2.subplots(1, 3, sharex=True)
for ax, (a0, base) in zip(axs, ((0.2, 2), (1.0, 0), (5.0, 10))):
    ax.set_title(f'linear_width={a0:.3g}')
    ax.plot(x, x, label='y=x')
    ax.plot(x, 10*x, label='y=10x')
    ax.plot(x, 100*x, label='y=100x')
    ax.set_yscale('asinh', linear_width=a0, base=base)
    ax.grid()
    ax.legend(loc='best', fontsize='small')
```
