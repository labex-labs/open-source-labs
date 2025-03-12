# 实现日志记录

在这一步中，我们将让你的代码更完善。不再使用简单的打印消息，而是使用 Python 的 `logging` 模块进行规范的日志记录。日志记录是跟踪程序运行情况的好方法，尤其是在处理错误和理解代码流程时。

## 理解日志记录模块

Python 中的 `logging` 模块为我们提供了一种灵活的方式，可从应用程序中输出日志消息。它比简单的打印语句强大得多。以下是它的功能：

1. 不同的日志级别（DEBUG、INFO、WARNING、ERROR、CRITICAL）：这些级别有助于我们对消息的重要性进行分类。例如，DEBUG 用于开发期间有用的详细信息，而 CRITICAL 用于可能导致程序停止的严重错误。
2. 可配置的输出格式：我们可以决定日志消息的显示方式，例如添加时间戳或其他有用信息。
3. 消息可定向到不同的输出（控制台、文件等）：我们可以选择在控制台显示日志消息、将其保存到文件，甚至发送到远程服务器。
4. 基于严重性的日志过滤：我们可以根据日志级别控制要查看的消息。

## 为 reader.py 添加日志记录

现在，让我们修改代码以使用日志记录模块。打开 `reader.py` 文件。

首先，我们需要导入 `logging` 模块，并为该模块设置一个日志记录器。在文件顶部添加以下代码：

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

`import logging` 语句引入了 `logging` 模块，以便我们可以使用其功能。`logging.getLogger(__name__)` 为这个特定模块创建了一个日志记录器。使用 `__name__` 可确保日志记录器具有与模块相关的唯一名称。

接下来，我们将修改 `convert_csv()` 函数，使用日志记录而不是打印语句。以下是更新后的代码：

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

这里的主要更改如下：

- 我们将 `print()` 替换为 `logger.warning()` 来输出错误消息。这样，消息会以适当的警告级别进行记录，并且我们可以在以后控制其可见性。
- 我们添加了一条新的 `logger.debug()` 消息，包含有关异常的详细信息。这为我们提供了更多关于出错原因的信息，但只有在日志级别设置为 DEBUG 或更低时才会显示。
- `str(e)` 将异常转换为字符串，以便我们可以在日志消息中显示错误原因。

完成这些更改后，保存文件。

## 测试日志记录

让我们在启用日志记录的情况下测试你的代码。在终端中运行以下命令打开 Python 解释器：

```bash
python3
```

进入 Python 解释器后，执行以下代码：

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

在这里，我们首先导入 `logging` 模块和我们的 `reader` 模块。然后，使用 `logging.basicConfig(level=logging.DEBUG)` 将日志级别设置为 DEBUG。这意味着我们将看到所有日志消息，包括 DEBUG、INFO、WARNING、ERROR 和 CRITICAL。然后，我们调用 `reader` 模块中的 `read_csv_as_dicts` 函数，并打印处理的有效行数。

你应该会看到如下输出：

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

注意，日志记录模块会为每条消息添加一个前缀，显示日志级别（WARNING/DEBUG）和模块名称。

现在，让我们看看如果将日志级别更改为仅显示警告会发生什么。在 Python 解释器中运行以下代码：

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

这次，我们使用 `logging.basicConfig(level=logging.WARNING)` 将日志级别设置为 WARNING。现在你只会看到 WARNING 消息，而 DEBUG 消息将被隐藏：

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

这显示了使用不同日志级别的优势。我们可以在不更改代码的情况下控制日志中显示的详细程度。

要退出 Python 解释器，运行以下命令：

```python
exit()
```

恭喜！你现在已经在 Python 程序中实现了规范的异常处理和日志记录。这使你的代码更可靠，并在出现错误时为你提供更详细的信息。
