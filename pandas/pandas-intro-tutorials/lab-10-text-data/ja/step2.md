# 文字列を小文字に変換する

次に、`Name`列のすべての文字を小文字に変換します。これを達成するために、`str.lower()`メソッドを使用します。

```python
# 'Name'列のすべての文字を小文字に変換する
titanic["Name"] = titanic["Name"].str.lower()
```
