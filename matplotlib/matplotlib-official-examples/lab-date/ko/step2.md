# 데이터 로드

다음으로, 플롯하려는 데이터를 로드합니다. `mpl-data/sample_data` 디렉토리에서 날짜, 시가, 고가, 저가, 종가, 거래량, 수정 종가 (adj_close) 필드가 있는 Yahoo CSV 데이터에서 numpy record array 를 사용합니다. record array 는 날짜 열에서 'D' 단위로 np.datetime64 로 날짜를 저장합니다.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
