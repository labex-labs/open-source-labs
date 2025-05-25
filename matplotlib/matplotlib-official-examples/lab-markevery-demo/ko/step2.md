# 선형 스케일로 플롯 생성

다음으로, `markevery`가 선형 스케일에서 어떻게 동작하는지 보여주기 위해 일련의 서브플롯을 생성합니다. `cases` 리스트를 반복하고 각 경우를 별도의 서브플롯에 플롯합니다. `markevery` 매개변수를 사용하여 표시할 데이터 포인트를 지정합니다.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
