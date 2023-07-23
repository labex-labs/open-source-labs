# Load the Financial Data

First, we need to load some financial data for Google's stock price using the Matplotlib `cbook.get_sample_data()` function. We will use the last 250 days of data.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load some financial data; Google's stock price
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # get the last 250 days
```
