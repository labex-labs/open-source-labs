# 使用元组处理结构化数据

到目前为止，我们一直在处理原始文本数据的存储。但在进行数据分析时，我们通常需要将数据转换为更有条理和结构化的格式。这样可以更轻松地执行各种操作，并从数据中获取有价值的信息。在这一步中，我们将学习如何使用 `csv` 模块将数据读取为元组列表。元组是 Python 中一种简单而实用的数据结构，可以容纳多个值。

## 创建使用元组的读取函数

让我们在 `/home/labex/project` 目录下创建一个名为 `readrides.py` 的新文件。这个文件将包含从 CSV 文件中读取数据并将其存储为元组列表的代码。

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    以元组列表的形式读取公交出行数据
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
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

这个脚本定义了一个名为 `read_rides_as_tuples` 的函数。下面是它的具体步骤：

1. 打开由 `filename` 参数指定的 CSV 文件，这样我们就可以访问文件中的数据。
2. 使用 `csv` 模块解析文件的每一行。`csv.reader` 函数帮助我们将每行拆分为单个值。
3. 从每行中提取四个字段（线路、日期、日期类型和乘客数量）。这些字段对我们的数据分析很重要。
4. 将 `rides` 字段转换为整数。这是必要的，因为 CSV 文件中的数据最初是字符串格式，而我们需要一个数值进行计算。
5. 创建一个包含这四个值的元组。元组是不可变的，这意味着一旦创建，它们的值就不能更改。
6. 将元组添加到名为 `records` 的列表中。这个列表将包含 CSV 文件中的所有记录。

现在，让我们运行这个脚本。打开终端并输入以下命令：

```bash
python3 /home/labex/project/readrides.py
```

你应该会看到类似以下的输出：

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

注意，与我们之前的示例相比，内存使用量增加了。这有几个原因：

1. 我们现在以结构化格式（元组）存储数据。结构化数据通常需要更多内存，因为它有明确的组织方式。
2. 元组中的每个值都是一个单独的 Python 对象。Python 对象有一定的开销，这导致了内存使用量的增加。
3. 我们有一个额外的列表结构来保存所有这些元组。列表也会占用内存来存储其元素。

使用这种方法的优点是，我们的数据现在已经正确结构化，并且可以进行分析。我们可以通过索引轻松访问每条记录的特定字段。例如：

```python
# 访问元组元素的示例（将此代码添加到 readrides.py 文件中进行尝试）
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

然而，通过数字索引访问数据并不总是直观的。尤其是在处理大量字段时，很难记住哪个索引对应哪个字段。在下一步中，我们将探索其他数据结构，使我们的代码更具可读性和可维护性。
