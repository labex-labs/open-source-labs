# Load data

Next, we will load the data that we want to plot. We will use a numpy record array from Yahoo csv data with fields date, open, high, low, close, volume, adj_close from the mpl-data/sample_data directory. The record array stores the date as an np.datetime64 with a day unit ('D') in the date column.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
