# 그림에 전역 x 및 y 레이블 추가

다음으로, 시간에 따른 서로 다른 회사의 상대적인 주가를 보여주는 그림에 전역 x 및 y 레이블을 추가합니다. `np.genfromtxt()` 함수를 사용하여 주가 데이터를 포함하는 CSV 파일을 읽은 다음, 서브플롯을 사용하여 각 회사에 대한 데이터를 플롯합니다. `fig.supxlabel()` 및 `fig.supylabel()` 메서드를 사용하여 그림에 전역 x 및 y 레이블을 추가합니다.

```python
from matplotlib.cbook import get_sample_data

with get_sample_data('Stocks.csv') as file:
    stocks = np.genfromtxt(
        file, delimiter=',', names=True, dtype=None,
        converters={0: lambda x: np.datetime64(x, 'D')}, skip_header=1)

fig, axs = plt.subplots(4, 2, figsize=(9, 5), layout='constrained',
                        sharex=True, sharey=True)
for nn, ax in enumerate(axs.flat):
    column_name = stocks.dtype.names[1+nn]
    y = stocks[column_name]
    line, = ax.plot(stocks['Date'], y / np.nanmax(y), lw=2.5)
    ax.set_title(column_name, fontsize='small', loc='left')
fig.supxlabel('Year')
fig.supylabel('Stock price relative to max')

plt.show()
```
