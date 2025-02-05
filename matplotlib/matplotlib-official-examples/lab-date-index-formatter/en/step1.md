# Import Required Libraries and Data

We first need to import the required libraries, which are `matplotlib`, `numpy`, and `matplotlib.cbook`. We also need to load a numpy record array from yahoo csv data with fields date, open, high, low, close, volume, adj_close from the mpl-data/sample_data directory. The record array stores the date as an np.datetime64 with a day unit ('D') in the date column. We will use this data to plot the financial time series.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load data from sample_data directory
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # get the first 9 days
```
