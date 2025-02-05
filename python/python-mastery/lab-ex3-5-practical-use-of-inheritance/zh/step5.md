# 使其更易于选择

使用继承的一个问题是选择不同类来使用时增加的复杂性（例如，记住类名、使用正确的 `import` 语句等）。一个工厂函数可以简化这一点。在你的 `tableformat.py` 文件中添加一个函数 `create_formatter()`，它允许用户通过指定格式（如 `'text'`、`'csv'` 或 `'html'`）更轻松地创建格式化器。例如：

```python
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('html')
>>> print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```

**讨论**

本练习中的 `TableFormatter` 类是所谓的“抽象基类”的一个示例。它不是打算直接使用的东西。相反，它作为程序组件（在这种情况下是各种输出格式）的一种接口规范。本质上，生成表格的代码将针对抽象基类进行编程，期望用户提供合适的实现。只要所有必需的方法都已实现，一切应该就“能正常工作”（但愿如此）。
