# 完成程序

现在，你要清理代码并创建 `pcost.py` 程序的最终版本。清理代码意味着移除任何不必要的部分，并确保输出结果美观。这是编程中的重要步骤，因为它能让你的代码更专业、更易理解。

你将从移除调试打印语句开始。这些语句在开发过程中用于检查变量的值和程序的流程，但在最终版本中并不需要。然后，你要确保最终输出的格式良好。

以下是 `pcost.py` 代码的最终版本：

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    try:
        # Open the file
        with open(filename, 'r') as file:
            # Read all lines in the file
            for line in file:
                # Strip any leading/trailing whitespace
                line = line.strip()

                # Skip empty lines
                if not line:
                    continue

                # Split the line into fields
                fields = line.split()

                # Extract the relevant data
                # fields[0] is the stock symbol (which we don't need for the calculation)
                shares = int(fields[1])  # Number of shares (second field)
                price = float(fields[2])  # Price per share (third field)

                # Calculate the cost of this stock purchase and add to the total
                total_cost += shares * price

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0.0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0.0

    # Return the total cost
    return total_cost

# Main block to run when the script is executed directly
if __name__ == '__main__':
    # Call the function with the portfolio file
    total_cost = portfolio_cost('portfolio.dat')
    print(f'Total cost: ${total_cost:.2f}')
```

这个最终版本的代码有几处改进：

1. 错误处理：添加了代码来捕获两种类型的错误。当指定的文件不存在时，会引发 `FileNotFoundError`。如果发生这种情况，程序将打印错误消息并返回 0.0。`Exception` 块捕获在处理文件时可能发生的任何其他错误。这使程序更健壮，减少了意外崩溃的可能性。
2. 格式规范：使用 f-string 中的 `:.2f` 格式说明符将总成本格式化为保留两位小数。这使输出看起来更专业、更易读。
3. `__name__ == '__main__'` 检查：这是常见的 Python 惯用法。它确保 `if` 块内的代码仅在脚本直接执行时运行。如果脚本作为模块导入到另一个脚本中，这段代码将不会运行。这让你能更好地控制脚本的行为。

现在，让我们运行最终代码。打开终端并输入以下命令：

```bash
python3 ~/project/pcost.py
```

运行此命令时，程序将读取 `portfolio.dat` 文件，计算投资组合的总成本，并打印结果。你应该会看到投资组合的总成本，应为 $44671.15。

恭喜！你已成功创建了一个 Python 程序，它能从文件中读取数据、处理数据并计算结果。这是一项了不起的成就，表明你正在成为一名熟练的 Python 程序员。
