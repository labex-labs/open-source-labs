# Reading Data From Excel

Reading data from an Excel file is as easy as reading data from a CSV file. We will use the `read_excel` function from pandas.

```python
# Reading data from an Excel file
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
```
