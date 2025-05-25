# 특정 승객 데이터 추출

다음으로, 타이타닉호에 탑승한 백작부인 (countesses) 의 승객 데이터를 추출해 보겠습니다. `str.contains()` 메서드를 사용하여 `Name` 열에 'Countess'라는 단어가 포함된 행을 찾습니다.

```python
# Find rows where 'Name' contains 'Countess'
countesses = titanic[titanic["Name"].str.contains("Countess")]
```
