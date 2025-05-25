# 테이블 행 정렬

타이타닉 데이터 세트를 승객의 나이별로 정렬한 다음, 객실 등급과 나이 순으로 내림차순으로 정렬합니다.

```python
# 나이별 정렬
titanic.sort_values(by="Age").head()

# Pclass 및 Age 를 내림차순으로 정렬
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
```
