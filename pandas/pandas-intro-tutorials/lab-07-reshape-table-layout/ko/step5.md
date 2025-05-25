# Wide 형식에서 Long 형식으로 변환

이제 `melt` 함수를 사용하여 𝑁𝑂2 의 wide 형식 데이터를 long 형식으로 변환해 보겠습니다.

```python
# no2_pivoted 의 인덱스 재설정
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# 데이터 멜트 (melt)
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
