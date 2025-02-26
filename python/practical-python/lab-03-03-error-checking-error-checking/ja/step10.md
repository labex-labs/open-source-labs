# 例外の再送出

キャッチしたエラーを伝播させるには、`raise` を使用します。

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

これにより、何らかのアクション（たとえば、ログ記録）を実行して、エラーを呼び出し元に渡すことができます。
