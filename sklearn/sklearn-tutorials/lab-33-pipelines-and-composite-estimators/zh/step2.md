# 嵌套参数

你可以使用 `<估计器>__<参数>` 的语法来访问管道中估计器的参数。这对于在管道中所有估计器的参数上进行网格搜索很有用。以下是一个示例：

```python
pipe.set_params(clf__C=10)
```
