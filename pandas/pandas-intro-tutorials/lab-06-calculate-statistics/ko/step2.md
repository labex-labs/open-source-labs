# 요약 통계 계산

이 단계에서는 타이타닉 데이터셋에 대한 요약 통계를 계산합니다.

```python
# 타이타닉 승객의 평균 나이 계산
average_age = titanic["Age"].mean()
# 결과 출력
print(f"타이타닉 승객의 평균 나이는 {average_age}입니다")

# 타이타닉 승객의 중앙값 나이 및 티켓 요금 계산
median_age_fare = titanic[["Age", "Fare"]].median()
# 결과 출력
print(f"타이타닉 승객의 중앙값 나이 및 티켓 요금은 {median_age_fare}입니다: {median_age_fare}")
```
