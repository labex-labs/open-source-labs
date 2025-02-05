# 模块加载

每个模块仅加载和执行**一次**。_注意：重复导入只会返回对先前加载模块的引用。_

`sys.modules` 是所有已加载模块的字典。

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__','site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath',...]
>>>
```

**注意**：如果你在更改模块的源代码后重复 `import` 语句，可能会产生常见的混淆。由于模块缓存 `sys.modules`，重复导入总是返回先前加载的模块 —— 即使进行了更改。将修改后的代码加载到 Python 中的最安全方法是退出并重新启动解释器。
