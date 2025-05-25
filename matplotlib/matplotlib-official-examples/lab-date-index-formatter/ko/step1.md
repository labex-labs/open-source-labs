# 필요한 라이브러리 및 데이터 가져오기

먼저 필요한 라이브러리인 `matplotlib`, `numpy`, `matplotlib.cbook`을 가져와야 합니다. 또한 mpl-data/sample_data 디렉토리에서 date, open, high, low, close, volume, adj_close 필드를 가진 yahoo csv 데이터로부터 numpy record array 를 로드해야 합니다. record array 는 날짜 열에서 일 단위 ('D') 로 np.datetime64 로 날짜를 저장합니다. 이 데이터를 사용하여 금융 시계열을 플로팅합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load data from sample_data directory
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # get the first 9 days
```
