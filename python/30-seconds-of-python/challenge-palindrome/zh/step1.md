# 回文

## 问题

编写一个函数 `palindrome(s)`，它接受一个字符串 `s` 作为唯一参数，如果 `s` 是回文则返回 `True`，否则返回 `False`。在检查回文时，你的函数应忽略大小写和非字母数字字符。

要解决这个问题，你可以按照以下步骤进行：

1. 使用 `str.lower()` 将字符串转换为小写。
2. 使用 `re.sub()` 从字符串中删除所有非字母数字字符。
3. 使用切片表示法将结果字符串与其反转后的字符串进行比较。

## 示例

```python
palindrome('taco cat') # True
palindrome('A man, a plan, a canal: Panama') # True
palindrome('hello world') # False
```
