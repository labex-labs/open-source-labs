# `fill_between`으로 선 그래프 향상시키기

첫 번째 예제에서는 `fill_between`을 사용하여 선 그래프를 향상시키는 방법을 보여줍니다. Google 의 금융 데이터를 사용하여 두 개의 서브플롯을 생성합니다. 하나는 단순한 선 그래프이고 다른 하나는 채워진 선 그래프입니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# load up some sample financial data
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# create two subplots with the shared x and y axes
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('price')
fig.suptitle('Google (GOOG) daily closing price')
fig.autofmt_xdate()
```
