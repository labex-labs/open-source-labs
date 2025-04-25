# 生産者 - 消費者問題

ジェネレータは、さまざまな形式の「生産者 - 消費者」問題と密接に関連しています。

```python
# 生産者
def follow(f):
 ...
    while True:
     ...
        yield line        # 以下の `line` の値を生成する
     ...

# 消費者
for line in follow(f):    # 上の `yield` から値を消費する
 ...
```

`yield` は、`for` が消費する値を生成します。
