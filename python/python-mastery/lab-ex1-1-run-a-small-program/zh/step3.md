# 创建一个更高级的 Python 程序

既然你已经掌握了 Python 的基础知识，现在是时候迈出下一步，创建一个更高级的 Python 程序了。这个程序将生成 ASCII 艺术图案，这些图案是由文本字符组成的简单但视觉上有趣的设计。通过编写这个程序，你将学习并应用几个重要的 Python 概念，例如导入模块、定义函数和处理命令行参数。

## 创建 ASCII 艺术程序

1. 首先，你需要在 WebIDE 中打开 `art.py` 文件。这个文件是在设置过程中创建的，你可以在 `/home/labex/project` 目录中找到它。打开这个文件是编写我们的 ASCII 艺术程序的起点。

2. 文件打开后，你可能会注意到其中有一些现有内容。我们需要清除这些内容，因为我们要从头开始编写自己的代码。所以，删除文件中的所有现有内容，然后将以下代码复制到 `art.py` 文件中。这段代码是我们 ASCII 艺术生成器的核心。

   ```python
   # art.py - A program to generate ASCII art patterns

   import sys
   import random

   # Characters used for the art pattern
   chars = '\|/'

   def draw(rows, columns):
       """
       Generate and print an ASCII art pattern with the specified dimensions.

       Args:
           rows: Number of rows in the pattern
           columns: Number of columns in the pattern
       """
       for r in range(rows):
           # For each row, create a string of random characters
           line = ''.join(random.choice(chars) for _ in range(columns))
           print(line)

   # This code only runs when the script is executed directly
   if __name__ == '__main__':
       # Check if the correct number of arguments was provided
       if len(sys.argv) != 3:
           print("Error: Incorrect number of arguments")
           print("Usage: python3 art.py rows columns")
           print("Example: python3 art.py 10 20")
           sys.exit(1)

       try:
           # Convert the arguments to integers
           rows = int(sys.argv[1])
           columns = int(sys.argv[2])

           # Call the draw function with the specified dimensions
           draw(rows, columns)
       except ValueError:
           print("Error: Both arguments must be integers")
           sys.exit(1)
   ```

3. 将代码复制到文件中后，保存你的工作非常重要。你可以通过按下键盘上的 Ctrl + S 组合键来保存，或者也可以转到菜单并选择“文件”>“保存”。保存文件可确保你的代码被存储并准备好运行。

## 理解代码

让我们仔细看看这个程序的功能。理解代码对于你将来能够修改和扩展它至关重要。

- **导入语句**：`import sys` 和 `import random` 这两行代码用于引入 Python 的内置模块。`sys` 模块提供了对 Python 解释器使用或维护的一些变量的访问，以及与解释器进行强交互的函数。`random` 模块允许我们生成随机数，我们将使用这些随机数来创建随机的 ASCII 艺术图案。
- **字符集**：`chars = '\|/'` 这行代码定义了用于创建我们的 ASCII 艺术的字符集。这些字符将被随机选择以形成图案。
- **`draw()` 函数**：这个函数负责创建 ASCII 艺术图案。它接受两个参数 `rows` 和 `columns`，用于指定图案的尺寸。在函数内部，它使用一个循环通过从 `chars` 字符集中随机选择字符来创建图案的每一行。
- **主程序块**：`if __name__ == '__main__':` 块是 Python 中的一个特殊结构。它确保该块内的代码仅在直接执行 `art.py` 文件时运行。如果该文件被导入到另一个 Python 文件中，这段代码将不会运行。
- **参数处理**：`sys.argv` 变量包含传递给程序的命令行参数。我们检查是否恰好提供了 3 个参数（脚本本身的名称加上两个表示行数和列数的数字）。这有助于确保用户提供了正确的输入。
- **错误处理**：`try/except` 块用于捕获可能发生的错误。如果用户提供了无效输入，例如行数和列数不是整数值，`try` 块将引发 `ValueError`，`except` 块将打印错误消息并退出程序。

## 运行程序

1. 要运行我们的程序，首先需要在 WebIDE 中打开一个终端。终端是我们输入命令来执行 Python 脚本的地方。

2. 终端打开后，我们需要导航到项目目录。这是我们的 `art.py` 文件所在的位置。在终端中使用以下命令：

   ```bash
   cd ~/project
   ```

   这个命令将当前工作目录更改为项目目录。

3. 现在我们已经位于正确的目录中，可以运行程序了。使用以下命令：

   ```bash
   python3 art.py 5 10
   ```

   这个命令告诉 Python 以 5 行 10 列的规格运行 `art.py` 脚本。当你运行这个命令时，你会在终端中看到一个 5×10 的字符图案。输出可能如下所示：

   ```
   |\//\\|\//
   /\\|\|//\\
   \\\/\|/|/\
   //|\\\||\|
   \|//|/\|/\
   ```

   请记住，实际的图案是随机的，所以你的输出会与这里显示的示例不同。

4. 你可以通过更改命令中的参数来尝试不同的尺寸。例如，尝试以下命令：

   ```bash
   python3 art.py 8 15
   ```

   这将生成一个更大的图案，包含 8 行 15 列。

5. 为了查看错误处理的效果，尝试提供无效参数。运行以下命令：

   ```bash
   python3 art.py
   ```

   你应该会看到类似以下的错误消息：

   ```
   Error: Incorrect number of arguments
   Usage: python3 art.py rows columns
   Example: python3 art.py 10 20
   ```

## 对代码进行实验

你可以通过修改字符集来让 ASCII 艺术图案更有趣。具体操作如下：

1. 再次在编辑器中打开 `art.py` 文件。我们将在这里对代码进行修改。

2. 在代码中找到 `chars` 变量，将其更改为使用不同的字符。例如，你可以使用以下代码：

   ```python
   chars = '*#@+.'
   ```

   这将更改用于创建 ASCII 艺术的字符集。

3. 进行更改后，再次使用 Ctrl + S 组合键或“文件”>“保存”来保存文件。然后，使用以下命令运行程序：

   ```bash
   python3 art.py 5 10
   ```

   现在你将看到一个使用新字符的不同图案。

这个练习展示了几个重要的 Python 概念，包括：

- 模块导入：如何从 Python 的内置模块中引入额外的功能。
- 函数定义：如何定义和使用函数来组织你的代码。
- 命令行参数处理：如何从命令行接受和处理用户输入。
- 使用 `try/except` 进行错误处理：如何在程序中优雅地处理错误。
- 字符串操作：如何创建和操作字符串以形成 ASCII 艺术图案。
- 随机数生成：如何生成随机值以创建独特的图案。
- 列表推导式：Python 中一种简洁的创建列表的方式，在 `draw()` 函数中使用。
