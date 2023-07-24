# Enhancing a Line Plot with `fill_between`

The first example demonstrates how to enhance a line plot with `fill_between`. We will use financial data from Google to create two subplots, one with a simple line plot and the other with a filled line plot.

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
