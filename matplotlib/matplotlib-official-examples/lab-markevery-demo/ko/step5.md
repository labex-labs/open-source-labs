# 극좌표 플롯 생성

마지막으로, `markevery`가 극좌표 플롯에서 어떻게 동작하는지 보여주기 위해 일련의 서브플롯을 생성합니다. 동작은 선형 스케일과 유사합니다.

```python
# create polar plots
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
