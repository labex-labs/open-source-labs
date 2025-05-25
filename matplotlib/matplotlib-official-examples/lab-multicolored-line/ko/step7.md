# 서브플롯 생성

색상으로 표시된 선분들을 보여주기 위해 서브플롯을 생성합니다. `matplotlib.pyplot`의 `subplots` 함수를 사용하여 2x1 그리드의 서브플롯을 생성하고, `sharex` 및 `sharey` 매개변수를 사용하여 서브플롯 간에 x 축과 y 축을 공유합니다.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
