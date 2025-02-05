# Add global x- and y-labels to a figure

Next, we will add global x- and y-labels to a figure showing the relative stock prices of different companies over time. We will use the `np.genfromtxt()` function to read in a CSV file containing stock price data and then plot the data for each company using subplots. We will use the `fig.supxlabel()` and `fig.supylabel()` methods to add global x- and y-labels to the figure.

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
