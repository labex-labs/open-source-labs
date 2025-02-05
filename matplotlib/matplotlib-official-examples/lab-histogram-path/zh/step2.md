# 设置随机种子并生成数据

我们将使用numpy生成随机数据。为了使我们的结果具有可重复性，我们将设置一个随机种子。在你的文件中添加以下代码：

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```
