# 열의 값 대체

마지막으로, `Sex` 열의 값을 대체해 보겠습니다: 'male'을 'M'으로, 'female'을 'F'로 변경합니다. 이를 위해 `replace()` 메서드를 사용합니다.

```python
# Replace 'male' with 'M' and 'female' with 'F' in the 'Sex' column
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
