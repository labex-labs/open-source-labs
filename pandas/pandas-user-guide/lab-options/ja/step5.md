# option_contextの使用

`option_context` 関数を使用すると、実行後に以前の設定に戻る一連のオプションでコード ブロックを実行できます。

```python
# Execute a code block with a set of options
with pd.option_context("display.max_rows", 10):
    # This will print 10 despite the global setting being different
    print(pd.get_option("display.max_rows"))

# This will print the global setting as the context block has ended
print(pd.get_option("display.max_rows"))
```
