# 准备数据

在这一步中准备图表的数据。我们将创建一个包含人员姓名、他们的表现以及错误率的列表。

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
