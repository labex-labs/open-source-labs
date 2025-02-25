# オプションの取得と設定

`pd.get_option` または `pd.set_option` をそれぞれ使用して、単一のオプションの値を取得または設定することができます。ここでは、最大表示行数を999に設定しています。

```python
# Get the current setting for maximum display rows
print(pd.options.display.max_rows)

# Set the maximum display rows to 999
pd.options.display.max_rows = 999

# Verify the new setting
print(pd.options.display.max_rows)
```
