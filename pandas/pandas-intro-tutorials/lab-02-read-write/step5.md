# Writing Data to Excel

You can also write the data to an Excel file using the `to_excel` method. Let's save our DataFrame to an Excel file.

```python
# Saving DataFrame to an Excel file
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
```
