# Excel 에서 데이터 읽기

Excel 파일에서 데이터를 읽는 것은 CSV 파일에서 데이터를 읽는 것만큼 쉽습니다. pandas 의 `read_excel` 함수를 사용합니다.

```python
# Excel 파일에서 데이터 읽기
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
