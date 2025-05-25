# 기본 통계 수행

Pandas 는 통계를 수행하기 위한 많은 기능을 제공합니다. 예를 들어, `max()`를 사용하여 열에서 최대값을 찾을 수 있습니다.

```python
# 최대 나이 찾기
df["Age"].max()
```

`describe()`를 사용하여 DataFrame 의 숫자 데이터에 대한 간략한 개요를 얻을 수도 있습니다.

```python
# 숫자 데이터 설명
df.describe()
```
