# オプションのリセット

1つ以上のオプションを既定値にリセットしたい場合は、`pd.reset_option` を使用できます。

```python
# Reset the maximum display rows to default
pd.reset_option("display.max_rows")

# Verify the reset
print(pd.options.display.max_rows)
```
