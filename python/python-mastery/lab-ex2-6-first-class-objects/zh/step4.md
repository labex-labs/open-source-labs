# 面向列的数据存储

到目前为止，我们一直将 CSV 数据存储为行字典列表。这意味着 CSV 文件中的每一行都表示为一个字典，其中键是列标题，值是该行中的相应数据。然而，在处理大型数据集时，这种方法可能效率不高。以面向列的格式存储数据可能是更好的选择。在面向列的方法中，每列的数据都存储在一个单独的列表中。这可以显著减少内存使用，因为相似的数据类型被分组在一起，并且对于某些按列聚合数据的操作，还可以提高性能。

## 创建面向列的数据读取器

现在，我们将创建一个新文件，帮助我们以面向列的格式读取 CSV 数据。在项目目录中创建一个名为 `colreader.py` 的新文件，并添加以下代码：

```python
import csv

class DataCollection:
    def __init__(self, headers, columns):
        """
        Initialize a column-oriented data collection.

        Parameters:
        headers (list): Column header names
        columns (dict): Dictionary mapping header names to column data lists
        """
        self.headers = headers
        self.columns = columns
        self._length = len(columns[headers[0]]) if headers else 0

    def __len__(self):
        """Return the number of rows in the collection."""
        return self._length

    def __getitem__(self, index):
        """
        Get a row by index, presented as a dictionary.

        Parameters:
        index (int): Row index

        Returns:
        dict: Dictionary representing the row at the given index
        """
        if isinstance(index, int):
            if index < 0 or index >= self._length:
                raise IndexError("Index out of range")

            return {header: self.columns[header][index] for header in self.headers}
        else:
            raise TypeError("Index must be an integer")

def read_csv_as_columns(filename, types):
    """
    Read a CSV file into a column-oriented data structure, converting each field
    according to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    DataCollection: Column-oriented data collection representing the CSV data
    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        # Initialize columns
        columns = {header: [] for header in headers}

        # Read data into columns
        for row in rows:
            # Convert values according to the specified types
            converted_values = [func(val) for func, val in zip(types, row)]

            # Add each value to its corresponding column
            for header, value in zip(headers, converted_values):
                columns[header].append(value)

    return DataCollection(headers, columns)
```

这段代码做了两件重要的事情：

1. 定义了一个 `DataCollection` 类。这个类以列的形式存储数据，但允许我们像处理行字典列表一样访问数据。这很有用，因为它提供了一种熟悉的方式来处理数据。
2. 定义了一个 `read_csv_as_columns` 函数。这个函数从文件中读取 CSV 数据，并将其存储在面向列的结构中。它还根据我们提供的类型转换 CSV 文件中的每个字段。

## 测试面向列的读取器

让我们使用 CTA 公交数据来测试我们的面向列的读取器。首先，打开 Python 解释器。你可以在终端中运行以下命令来实现：

```bash
python3
```

Python 解释器打开后，运行以下代码：

```python
import colreader
import tracemalloc
from sys import intern

# Start memory tracking
tracemalloc.start()

# Read data into column-oriented structure with string interning
data = colreader.read_csv_as_columns('ctabus.csv', [intern, intern, intern, int])

# Check that we can access the data like a list of dictionaries
print(f"Number of rows: {len(data)}")
print("First 3 rows:")
for i in range(3):
    print(data[i])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

输出应该如下所示：

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

现在，让我们将其与之前的面向行的方法进行比较。在同一个 Python 解释器中运行以下代码：

```python
import reader
import tracemalloc
from sys import intern

# Reset memory tracking
tracemalloc.reset_peak()

# Read data into row-oriented structure with string interning
rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, intern, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (row-oriented): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (row-oriented): {peak / 1024 / 1024:.2f} MB")
```

输出应该类似于：

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

如你所见，面向列的方法使用的内存显著减少！

让我们还测试一下我们仍然可以像以前一样分析数据。运行以下代码：

```python
# Find all unique routes in the column-oriented data
routes = {row['route'] for row in data}
print(f"Number of unique routes: {len(routes)}")

# Count rides per route (first 5)
from collections import defaultdict
route_rides = defaultdict(int)
for row in data:
    route_rides[row['route']] += row['rides']

# Show the top 5 routes by total rides
top_routes = sorted(route_rides.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 routes by total rides:")
for route, rides in top_routes:
    print(f"Route {route}: {rides:,} rides")
```

输出应该是：

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

最后，通过运行以下命令退出 Python 解释器：

```python
exit()
```

我们可以看到，面向列的方法不仅节省了内存，还允许我们执行与以前相同的分析。这表明不同的数据存储策略如何在为我们提供相同的数据操作接口的同时，对性能产生重大影响。
