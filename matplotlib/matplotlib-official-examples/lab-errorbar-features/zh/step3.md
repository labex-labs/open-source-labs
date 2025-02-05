# 定义误差值

现在我们将定义误差值。在这个例子中，我们将使用`error`变量来表示对称误差，使用`asymmetric_error`变量来表示不对称误差。

```python
# 示例误差线值，其随x位置变化
error = 0.1 + 0.2 * x

# 具有不同正负误差的误差线值，
# 且也随x位置变化
lower_error = 0.4 * error
upper_error = error
asymmetric_error = [lower_error, upper_error]
```
