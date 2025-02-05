# 返回多个值

假设你正在编写代码来解析由如下行组成的配置文件：

    name=value

编写一个函数 `parse_line(line)`，它接受这样一行内容，并返回相关联的名称和值。返回多个值的常见约定是将它们作为一个元组返回。例如：

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> name, val = parse_line('email=guido@python.org')
>>> name
'email'
>>> val
'guido@python.org'
>>>
```
