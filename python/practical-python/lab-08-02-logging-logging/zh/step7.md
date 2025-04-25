# 练习 8.2：向模块添加日志记录

在`fileparse.py`中，有一些与错误输入导致的异常相关的错误处理。它看起来像这样：

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    将 CSV 文件解析为具有类型转换的记录列表。
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # 读取文件头（如果有）
    headers = next(rows) if has_headers else []

    # 如果选择了特定列，创建用于过滤的索引并设置输出列
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # 跳过无数据的行
            continue

        # 如果选择了特定列索引，挑选出这些列
        if select:
            row = [ row[index] for index in indices]

        # 对行应用类型转换
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"第{rowno}行：无法转换 {row}")
                    print(f"第{rowno}行：原因 {e}")
                continue

        # 创建字典或元组
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

注意那些发出诊断消息的打印语句。用日志记录操作替换这些打印相对简单。将代码修改如下：

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    将 CSV 文件解析为具有类型转换的记录列表。
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # 读取文件头（如果有）
    headers = next(rows) if has_headers else []

    # 如果选择了特定列，创建用于过滤的索引并设置输出列
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # 跳过无数据的行
            continue

        # 如果选择了特定列索引，挑选出这些列
        if select:
            row = [ row[index] for index in indices]

        # 对行应用类型转换
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("第 %d 行：无法转换 %s", rowno, row)
                    log.debug("第 %d 行：原因 %s", rowno, e)
                continue

        # 创建字典或元组
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

现在你已经做了这些更改，尝试在错误数据上使用你的一些代码。

```python
>>> import report
>>> a = report.read_portfolio('missing.csv')
第4行：错误的行：['MSFT', '', '51.23']
第7行：错误的行：['IBM', '', '70.44']
>>>
```

如果你不做任何操作，你只会得到`WARNING`级别及以上的日志消息。输出看起来会像简单的打印语句。然而，如果你配置日志记录模块，你会得到关于日志级别、模块等的更多信息。按以下步骤操作来查看：

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:第4行：无法转换 ['MSFT', '', '51.23']
WARNING:fileparse:第7行：无法转换 ['IBM', '', '70.44']
>>>
```

你会注意到看不到`log.debug()`操作的输出。输入以下内容来更改级别。

```python
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('missing.csv')
WARNING:fileparse:第4行：无法转换 ['MSFT', '', '51.23']
DEBUG:fileparse:第4行：原因：invalid literal for int() with base 10: ''
WARNING:fileparse:第7行：无法转换 ['IBM', '', '70.44']
DEBUG:fileparse:第7行：原因：invalid literal for int() with base 10: ''
>>>
```

关闭所有日志消息，只保留最关键的：

```python
>>> logging.getLogger('fileparse').setLevel(logging.CRITICAL)
>>> a = report.read_portfolio('missing.csv')
>>>
```
