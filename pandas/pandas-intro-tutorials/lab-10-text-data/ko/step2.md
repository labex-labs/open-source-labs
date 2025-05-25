# 문자열 문자를 소문자로 변환

다음으로, `Name` 열의 모든 문자를 소문자로 변환합니다. `str.lower()` 메서드를 사용하여 이를 수행합니다.

```python
# Convert all characters in the 'Name' column to lowercase
titanic["Name"] = titanic["Name"].str.lower()
```
