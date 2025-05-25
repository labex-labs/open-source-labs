# 데이터 로드

mpl-data/sample_data 디렉토리에서 date, open, high, low, close, volume, adj_close 필드를 가진 yahoo csv 데이터로부터 numpy record array 를 로드합니다. record array 는 date 열에서 날짜를 'D' 단위의 np.datetime64 로 저장합니다.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```
