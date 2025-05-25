# PyArrow 연산

PyArrow 데이터 구조 통합은 pandas 의 ExtensionArray 인터페이스를 통해 구현됩니다. 이 인터페이스가 pandas API 내에 통합된 경우 지원되는 기능이 존재합니다.

```python
# Create a pandas Series with PyArrow data type
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# Perform various operations
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
