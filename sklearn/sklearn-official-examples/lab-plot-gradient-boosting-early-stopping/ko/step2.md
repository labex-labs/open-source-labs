# 데이터 준비

다음으로, 데이터를 학습용 및 테스트용 집합으로 분할하여 데이터를 준비합니다.

```python
for X, y in data_list:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
```
