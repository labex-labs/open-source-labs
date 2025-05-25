# 누락된 값 및 채우기 값 사용하기

`missing_values` 및 `filling_values` 인수는 누락된 데이터를 처리하는 데 사용됩니다. `missing_values` 인수는 누락된 데이터를 인식하는 데 사용되며, `filling_values` 인수는 누락된 항목에 대한 값을 제공하는 데 사용됩니다.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
