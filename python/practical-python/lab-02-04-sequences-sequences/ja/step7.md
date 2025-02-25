# continue 文

1 つの要素をスキップして次の要素に移動するには、`continue` 文を使用します。

```python
for line in lines:
    if line == '\n':    # 空行をスキップする
        continue
    # その他の文
 ...
```

これは、現在の項目が関心対象外である場合や、処理で無視する必要がある場合に便利です。
