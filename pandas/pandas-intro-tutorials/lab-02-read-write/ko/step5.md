# 데이터를 Excel 로 쓰기

`to_excel` 메서드를 사용하여 데이터를 Excel 파일로 쓸 수도 있습니다. 데이터프레임을 Excel 파일로 저장해 보겠습니다.

```python
# 데이터프레임을 Excel 파일로 저장
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
