# 列の値を置き換える

最後に、`Sex`列の値を置き換えましょう。「male」を「M」に、「female」を「F」に置き換えます。これには`replace()`メソッドを使用します。

```python
# 'Sex'列の'male'を'M'に、'female'を'F'に置き換える
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
