# 금융 데이터 로드

먼저, Matplotlib 의 `cbook.get_sample_data()` 함수를 사용하여 Google 주식 가격에 대한 금융 데이터를 로드해야 합니다. 마지막 250 일의 데이터를 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load some financial data; Google's stock price
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # get the last 250 days
```
