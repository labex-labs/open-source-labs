# 열 레이블을 소문자로 변환

마지막으로, 함수를 사용하여 열 레이블을 소문자로 변환합니다.

```python
# Convert column labels to lowercase
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```
