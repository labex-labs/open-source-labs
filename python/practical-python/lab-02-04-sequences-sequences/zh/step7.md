# continue 语句

要跳过一个元素并移动到下一个元素，请使用 `continue` 语句。

```python
for line in lines:
    if line == '\n':    # 跳过空行
        continue
    # 更多语句
 ...
```

当当前项目不感兴趣或在处理过程中需要忽略时，这很有用。
