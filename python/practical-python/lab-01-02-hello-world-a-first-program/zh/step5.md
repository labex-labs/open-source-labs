# 一个示例程序

让我们解决以下问题：

> 一天早上，你出门并在芝加哥西尔斯大厦旁的人行道上放了一张一美元的钞票。此后的每一天，你出门时都会将钞票的数量翻倍。那么需要多长时间这堆钞票的高度才能超过这座大厦的高度？

以下是在 `/home/labex/project` 目录中创建一个 `sears.py` 文件的解决方案：

```python
# sears.py
bill_thickness = 0.11 * 0.001 # 米（0.11 毫米）
sears_height = 442 # 高度（米）
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('天数', day)
print('钞票数量', num_bills)
print('最终高度', num_bills * bill_thickness)
```

当你运行它时，会得到以下输出：

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
天数 23
钞票数量 4194304
最终高度 461.37344
```

以这个程序为指导，你可以学习到一些关于 Python 的重要核心概念。
