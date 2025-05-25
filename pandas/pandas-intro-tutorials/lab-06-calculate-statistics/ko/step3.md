# 범주별 통계 집계

다음으로, 범주별로 그룹화된 통계를 집계하는 방법을 배우겠습니다.

```python
# 남성 대 여성 타이타닉 승객의 평균 나이 계산
average_age_sex = titanic[["Sex", "Age"]].groupby("Sex").mean()
# 결과 출력
print(f"남성 대 여성 타이타닉 승객의 평균 나이는 {average_age_sex}입니다")

# 각 성별 및 객실 등급 조합에 대한 평균 티켓 요금 계산
mean_fare_sex_class = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
# 결과 출력
print(f"각 성별 및 객실 등급 조합에 대한 평균 티켓 요금은 {mean_fare_sex_class}입니다")
```
