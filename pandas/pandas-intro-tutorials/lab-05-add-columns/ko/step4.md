# 열 레이블 이름 변경

OpenAQ 에서 사용하는 스테이션 식별자와 일치하도록 열 레이블의 이름을 변경합니다.

```python
# Rename column labels
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
```
