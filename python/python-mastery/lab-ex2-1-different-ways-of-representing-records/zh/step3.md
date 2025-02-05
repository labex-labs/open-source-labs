# 元组列表

在实际应用中，你可能会将数据读入列表，并将每一行转换为其他数据结构。下面是一个名为 `readrides.py` 的程序，它使用 `csv` 模块将整个文件读入元组列表：

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    将公交乘车数据读取为元组列表
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # 跳过标题行
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
```

使用 `python3 -i readrides.py` 运行此程序，并查看 `rows` 的结果内容。你应该会得到一个如下所示的元组列表：

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

查看结果中的内存使用情况。它应该比步骤2中的内存使用量高得多。
