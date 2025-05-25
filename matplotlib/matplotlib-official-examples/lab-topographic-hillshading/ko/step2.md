# 데이터 로드

다음으로, Matplotlib 의 `get_sample_data` 함수를 사용하여 샘플 고도 데이터를 로드합니다. 그런 다음 고도 데이터와 그리드의 셀 크기를 추출합니다.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
