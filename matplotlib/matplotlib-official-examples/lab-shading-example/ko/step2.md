# 데이터 로드

다음으로, 이 튜토리얼에 사용할 샘플 데이터를 로드합니다. 고도 데이터를 포함하는 `jacksboro_fault_dem.npz` 파일을 사용합니다.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
