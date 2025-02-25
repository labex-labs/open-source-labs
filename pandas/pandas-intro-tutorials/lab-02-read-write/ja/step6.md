# Excel ファイルからのデータ読み込み

Excel ファイルからデータを読み込むことは、CSV ファイルからデータを読み込むのと同じくらい簡単です。pandas の `read_excel` 関数を使用します。

```python
# Reading data from an Excel file
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
