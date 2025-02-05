# 模块拆分

`structly/tableformat.py` 文件包含用于创建不同格式表格的代码。具体如下：

- 一个 `TableFormatter` 基类。
- 一个 `TextTableFormatter` 类。
- 一个 `CSVTableFormatter` 类。
- 一个 `HTMLTableFormatter` 类。

与其将所有这些类放在一个 `.py` 文件中，或许将每个具体的格式化器移到它自己的文件中会更有意义。要做到这一点，我们将把 `tableformat.py` 文件拆分成几个部分。请仔细按照以下说明操作：

首先，删除 `structly/__pycache__` 目录。

    % cd structly
    % rm -rf __pycache__

接下来，创建目录 `structly/tableformat`。这个目录的名称必须与它所替代的模块（`tableformat.py`）完全相同。

```bash
mkdir tableformat
```

将原来的 `tableformat.py` 文件移动到新的 `tableformat` 目录中，并将其重命名为 `formatter.py`。

```bash
mv tableformat.py tableformat/formatter.py
```

在 `tableformat` 目录中，将 `tableformat.py` 代码拆分为以下文件和目录：

- `formatter.py` - 包含 `TableFormatter` 基类、混入类和各种函数。
- `formats/text.py` - 包含 `TextTableFormatter` 类。
- `formats/csv.py` - 包含 `CSVTableFormatter` 类。
- `formats/html.py` - 包含 `HTMLTableFormatter` 类。

在 `tableformat/` 和 `tableformat/formats` 目录中添加一个 `__init__.py` 文件。让 `tableformat/__init__.py` 导出与原来的 `tableformat.py` 文件相同的符号。

在你进行了所有这些更改之后，你应该拥有一个如下所示的包结构：

    structly/
          __init__.py
          validate.py
          reader.py
          structure.py
          tableformat/
               __init__.py
               formatter.py
               formats/
                   __init__.py
                   text.py
                   csv.py
                   html.py

对于用户来说，一切应该和以前完全一样正常工作。例如，你之前的 `stock.py` 文件应该能正常运行：

```python
# stock.py

from structly import *

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
