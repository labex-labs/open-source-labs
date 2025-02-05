# 字符串方法

字符串有一些方法可对字符串数据执行各种操作。

示例：去除任何前导/尾随空白字符。

```python
s =' Hello '
t = s.strip()     # 'Hello'
```

示例：大小写转换。

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

示例：替换文本。

```python
s = 'Hello world'
t = s.replace('Hello ', 'Hallo')   # 'Hallo world'
```

**更多字符串方法**：

字符串还有许多其他用于测试和操作文本数据的方法。以下是一小部分方法：

```python
s.endswith(suffix)     # 检查字符串是否以suffix结尾
s.find(t)              # 在s中首次出现t的位置
s.index(t)             # 在s中首次出现t的位置
s.isalpha()            # 检查字符是否为字母
s.isdigit()            # 检查字符是否为数字
s.islower()            # 检查字符是否为小写
s.isupper()            # 检查字符是否为大写
s.join(slist)          # 使用s作为分隔符连接字符串列表
s.lower()              # 转换为小写
s.replace(old,new)     # 替换文本
s.rfind(t)             # 从字符串末尾开始搜索t
s.rindex(t)            # 从字符串末尾开始搜索t
s.split([delim])       # 将字符串拆分为子字符串列表
s.startswith(prefix)   # 检查字符串是否以prefix开头
s.strip()              # 去除前导/尾随空格
s.upper()              # 转换为大写
```
