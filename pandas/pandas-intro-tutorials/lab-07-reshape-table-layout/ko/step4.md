# 피벗 테이블 생성

각 스테이션에서 𝑁𝑂2 및 𝑃𝑀25 의 평균 농도를 찾기 위해 피벗 테이블을 생성합니다.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```
