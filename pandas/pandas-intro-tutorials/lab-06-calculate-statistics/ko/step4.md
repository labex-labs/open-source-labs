# 범주별 레코드 수 계산

마지막으로, 범주별 레코드 수를 계산합니다.

```python
# 각 객실 등급의 승객 수 계산
passengers_per_class = titanic["Pclass"].value_counts()
# 결과 출력
print(f"각 객실 등급의 승객 수는 {passengers_per_class}입니다")
```
