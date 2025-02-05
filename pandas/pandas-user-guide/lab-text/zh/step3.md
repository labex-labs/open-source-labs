# 提取子字符串

你可以使用正则表达式提取子字符串。`extract`方法接受一个至少包含一个捕获组的正则表达式。

```python
# 从每个字符串中提取第一个数字
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
