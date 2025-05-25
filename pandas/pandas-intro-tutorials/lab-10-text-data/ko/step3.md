# 전체 이름에서 성 추출

이제 승객의 성을 포함하는 새로운 열 `Surname`을 생성해 보겠습니다. `Name` 열에서 쉼표 앞부분을 추출하여 이를 수행합니다.

```python
# Split the 'Name' column on comma and extract the first part
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
```
